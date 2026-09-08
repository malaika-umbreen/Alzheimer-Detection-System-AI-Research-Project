from datetime import datetime
from flask_login import LoginManager, UserMixin
from flask import Flask, render_template, request, redirect, url_for, session
from keras.models import load_model
from keras.preprocessing import image
from keras.metrics import AUC
from PIL import Image
import numpy as np
import re
# import pyrebase
from tensorflow.keras.utils import img_to_array
# from config import firebase_config
import MySQLdb.cursors
from flask_mysqldb import MySQL
from flask import flash


app = Flask(__name__)
 
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'alzheimer_db'
app.config['SECRET_KEY'] = '123'
mysql = MySQL(app)


login_manager = LoginManager(app)
login_manager.login_view = 'login'

class User(UserMixin):
    pass

@login_manager.user_loader
def load_user(user_id):
    user = User()
    user.id = user_id
    return user


verbose_name = {
    0: "Non Demented",
    1: "Very Mild Demented",
    2: "Mild Demented",
    3: "Moderate Demented",
}

# Select model
model = load_model("alzheimer_cnn_model.h5", compile=False)



def predict_label(img_path):
    # Open and convert the image to grayscale ("L" mode)
    test_image = Image.open(img_path).convert("L")
    
    # Resize the image to 128x128 (assuming the model expects this size)
    test_image = test_image.resize((128, 128))
    
    # Convert the image to a NumPy array and normalize pixel values
    test_image = img_to_array(test_image) / 255.0
    
    # Reshape the image for the model (batch_size, height, width, channels)
    test_image = np.reshape(test_image, (-1, 128, 128, 1))
    
    # Get predictions from the model
    predict_x = model.predict(test_image)
    
    # Get the index of the highest probability class
    classes_x = np.argmax(predict_x, axis=1)
    
    # Return the class label based on the model's prediction
    return verbose_name[classes_x[0]]



# @app.route("/", methods=["GET", "POST"])
# def main():
#     return render_template("index.html")

@app.route("/", methods=["GET", "POST"])
def main():
    if 'username' in session:
        return render_template('index.html')
    else:
        return redirect(url_for('login'))




@app.route('/history')
def history():
    if 'loggedin' not in session:
        flash("Please log in to view history", "warning")
        return redirect(url_for('login'))
    
    user_id = session['id']
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT * FROM prediction_history WHERE user_id = %s ORDER BY timestamp DESC', (user_id,))
    history_data = cursor.fetchall()
    cursor.close()
    
    return render_template("history.html", history=history_data)


@app.route('/login/', methods=['GET', 'POST'])
def login():
# Output message if something goes wrong...
    # Check if "username" and "password" POST requests exist (user submitted form)
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        # Create variables for easy access
        username = request.form['username']
        password = request.form['password']
        # Check if account exists using MySQL
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM users WHERE username = %s AND password = %s', (username, password))
        # Fetch one record and return result
        account = cursor.fetchone()
                # If account exists in accounts table in out database
        if account:
            # Create session data, we can access this data in other routes
            session['loggedin'] = True
            session['id'] = account['id']
            session['username'] = account['username']
            # Redirect to home page
            return redirect(url_for('index'))
        else:
            # Account doesnt exist or username/password incorrect
            flash("Incorrect username/password!", "danger")
    return render_template('auth/login.html',title="Login")

@app.route('/auth/register', methods=['GET', 'POST'])
def register():
    # Check if "username", "password" and "email" POST requests exist (user submitted form)
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form:
        # Create variables for easy access
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
                # Check if account exists using MySQL
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        # cursor.execute('SELECT * FROM users WHERE username = %s', (username))
        cursor.execute( "SELECT * FROM users WHERE username LIKE %s", [username] )
        account = cursor.fetchone()
        # If account exists show error and validation checks
        if account:
            flash("Account already exists!", "danger")
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            flash("Invalid email address!", "danger")
        elif not re.match(r'[A-Za-z0-9]+', username):
            flash("Username must contain only characters and numbers!", "danger")
        elif not username or not password or not email:
            flash("Incorrect username/password!", "danger")
        else:
        # Account doesnt exists and the form data is valid, now insert new account into accounts table
            cursor.execute('INSERT INTO users VALUES (NULL, %s, %s, %s)', (username,email, password))
            mysql.connection.commit()
            flash("You have successfully registered!", "success")
            return redirect(url_for('login'))

    elif request.method == 'POST':
        # Form is empty... (no POST data)
        flash("Please fill out the form!", "danger")
    # Show registration form with message (if any)
    return render_template('./auth/register.html',title="Register")



@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))



@app.route('/')
def index():
    if 'username' in session:
        return render_template('index.html')
    else:
        return redirect(url_for('login'))




@app.route("/submit", methods=["GET", "POST"])
def get_output():
    if request.method == "POST":
        if 'loggedin' in session:
            user_id = session['id']
        else:
            flash("Please log in to make a prediction", "warning")
            return redirect(url_for('login'))
        
        img = request.files["my_image"]
        img_path = "static/tests/" + img.filename
        img.save(img_path)
        
        test_image = Image.open(img_path)
        
        if test_image.mode != "L":
            error_message = "Only Alzheimer (X-ray) images are accepted. Please upload a valid Alzheimer X-ray image."
            return render_template("index.html", error=error_message)
        
        predict_result = predict_label(img_path)
        
        # Save prediction to database
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute(
            'INSERT INTO prediction_history (user_id, image_path, prediction, timestamp) VALUES (%s, %s, %s, %s)',
            (user_id, img_path, predict_result, datetime.now())
        )
        mysql.connection.commit()
        cursor.close()
        
        return render_template("index.html", prediction=predict_result, img_path=img_path)

    return render_template("index.html")



if __name__ == "__main__":
    app.run(debug=True)
