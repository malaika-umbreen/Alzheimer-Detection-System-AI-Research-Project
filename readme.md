# 🧠 Alzheimer's Disease Detection System

A deep learning-powered web application for early detection and classification of Alzheimer's Disease from MRI brain scans using a Convolutional Neural Network (CNN) ResNet50 model.

---

## 📌 Table of Contents

- [Overview](#overview)
- [Demo](#demo)
- [Features](#features)
- [Project Structure](#project-structure)
- [Dataset](#dataset)
- [Model](#model)
- [Tech Stack](#tech-stack)
- [Installation & Setup](#installation--setup)
- [Database Setup](#database-setup)
- [Usage](#usage)
- [Results](#results)
- [Contributing](#contributing)
- [License](#license)

---

## 🔍 Overview

This project is a full-stack web application that uses a trained CNN model to classify Alzheimer's Disease severity from MRI brain scan images. It allows users to upload MRI images and receive an instant prediction with one of four dementia severity classes.

The system includes user authentication, prediction history tracking, and a clean web interface — all backed by a Python/Flask backend and MySQL database.

---

## ✨ Features

- 🔐 User Registration & Login (with session management)
- 🧠 MRI Image Upload & CNN-based Prediction
- 📊 4-Class Alzheimer's Classification
- 📁 Prediction History per User
- 🎨 Responsive Web Interface
- 🗄️ MySQL Database via XAMPP

---

## 📂 Project Structure

```
Alzheimer-Detection-System-AI-Research-Project/
│
├── Dataset/
│   └── MildDemented/
|   └── ModerateDemented/
|   └── NonDemented/
|   └── VeryMildDemented/
|
├── Database/
│   └── alzheimer_db.sql              # MySQL database schema & seed data
|
├── model/
│   └── Alzhimer_Disease_Code.ipynb   # Jupyter/Colab notebook for model training
│
├── static/
│   ├── assets/                   # Images, icons, fonts
│   ├── tests/                    # Static test resources
│   └── style.css                 # Global stylesheet
│
├── templates/
│   ├── auth/                     # Authentication templates
│   ├── includes/                 # Reusable template components (header, footer)
│   ├── history.html              # Prediction history page
│   ├── index.html                # Home / Upload page
│   ├── login.html                # Login page
│   ├── previous_results.html     # Past results page
│   └── register.html             # Registration page
│
├── alzheimer_cnn_model.h5        # Pre-trained CNN model weights
└── app.py                        # Main Flask application
```

---

## 🗂️ Dataset

The dataset used for training is an MRI brain scan image dataset organized into **4 classes** based on Alzheimer's severity:

| Class | Description |
|-------|-------------|
| `NonDemented` | No signs of dementia |
| `VeryMildDemented` | Very mild cognitive impairment |
| `MildDemented` | Mild Alzheimer's symptoms |
| `ModerateDemented` | Moderate Alzheimer's progression |

```
dataset/
├── MildDemented/
├── ModerateDemented/
├── NonDemented/
└── VeryMildDemented/
```

> **Note:** The dataset samples are included in this repository in Dataset folder.

---

## 🤖 Model

The CNN model was built and trained using TensorFlow/Keras in a Google Colab environment.

- **Architecture:** Convolutional Neural Network (CNN)
- **Input:** MRI brain scan images (resized to model input shape)
- **Output:** 4-class softmax classification
- **Saved Format:** `.h5` (Keras HDF5)
- **Training Notebook:** `model/Alzhimer_Disease_Code.ipynb`

To retrain the model, open the notebook in Google Colab and point it to your dataset directory.

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|------------|
| **Frontend** | HTML5, CSS3, Jinja2 Templates |
| **Backend** | Python, Flask |
| **ML Framework** | TensorFlow / Keras |
| **Database** | MySQL (via XAMPP) |
| **Model Training** | Google Colab (Jupyter Notebook) |
| **Server** | XAMPP (Apache + MySQL) |

---

## ⚙️ Installation & Setup

### Prerequisites

Make sure you have the following installed:

- Python 3.8+
- XAMPP (for MySQL)
- pip

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/alzheimer-detection-system.git
cd alzheimer-detection-system
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

> If `requirements.txt` is not present, install manually:

```bash
pip install flask tensorflow keras Pillow numpy mysql-connector-python
```

### 4. Add the Pre-trained Model

Ensure `alzheimer_cnn_model.h5` is in the root directory of the project. If missing, retrain using the Colab notebook in `model/`.

---

## 🗄️ Database Setup

This project uses **MySQL via XAMPP**.

### Steps:

1. Start **XAMPP** and enable **Apache** and **MySQL**.
2. Open **phpMyAdmin** at `http://localhost/phpmyadmin`.
3. Create a new database named `alzheimer_db`.
4. Import the SQL file:
   - Go to the **Import** tab
   - Select `Database/alzheimer_db.sql`
   - Click **Go**

### Update DB credentials in `app.py`:

```python
db = mysql.connector.connect(
    host="localhost",
    user="root",         # your MySQL username
    password="",         # your MySQL password (empty by default in XAMPP)
    database="alzheimer_db"
)
```

---

##  Usage

1. Make sure XAMPP MySQL is running.
2. Run the Flask application:

```bash
python app.py
```

3. Open your browser and go to:

```
http://127.0.0.1:5000
```

4. **Register** a new account or **Login** with existing credentials.
5. Upload an MRI brain scan image on the home page.
6. View the **prediction result** and classification.
7. Check **Prediction History** to view past uploads and results.

---

## 📊 Results

The CNN model was trained on MRI scan images across 4 classes. Below are the performance highlights:
\
| Metric | Value |
|--------|-------|
| Model Type | CNN (Custom) |
| Classes | 4 |
| Input Format | MRI Grayscale Images |
| Output | Class Label + Confidence |

> Detailed training metrics, accuracy curves, and confusion matrix are available inside the Colab notebook: `model/Alzhimer_Disease_Code.ipynb`

---

## 📸 Screenshots

> 

| Page | Preview |
|------|---------|
                                    | Home |

<img width="604" height="290" alt="image" src="https://github.com/user-attachments/assets/d55192b9-49f1-49c1-88b9-050953be39e2" />



                                    |About US  |  

<img width="622" height="298" alt="image" src="https://github.com/user-attachments/assets/3b128e90-45f9-4725-972a-e83827dac6c0" />



                                     |   Upload  |  


<img width="615" height="296" alt="image" src="https://github.com/user-attachments/assets/032d51c7-742e-4d98-b48d-34bca58f46aa" />



                                   |Prediction Result |  


<img width="561" height="306" alt="image" src="https://github.com/user-attachments/assets/0be1fad7-a080-4eca-8a5e-b8e8f592b0e3" />




                                     | History Page | 

<img width="564" height="305" alt="image" src="https://github.com/user-attachments/assets/ba333d44-03b4-4f1c-bd2b-ab1fad94ed18" />


---

## 🤝 Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Commit your changes: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin feature/your-feature`
5. Open a Pull Request

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 👤 Author

**Malaika Umbreen**    
🔗 [GitHub](https://github.com/MalaikaUmbreen) | [LinkedIn](https://linkedin.com/in/malaika-umbreen)

---

> ⚠️ **Disclaimer:** This tool is intended for Research and Educational purposes only. It is not a substitute for professional medical diagnosis.
