-- phpMyAdmin SQL Dump
-- version 4.8.3
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 03, 2024 at 07:38 AM
-- Server version: 10.1.36-MariaDB
-- PHP Version: 7.0.32

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `alzheimer_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `prediction_history`
--

CREATE TABLE `prediction_history` (
  `id` int(11) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  `image_path` varchar(255) DEFAULT NULL,
  `prediction` varchar(50) DEFAULT NULL,
  `timestamp` datetime DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `prediction_history`
--

INSERT INTO `prediction_history` (`id`, `user_id`, `image_path`, `prediction`, `timestamp`) VALUES
(1, 1, 'static/tests/moderate_3.jpg', 'Moderate Demented', '2024-10-28 13:32:09'),
(2, 1, 'static/tests/mild_104.jpg', 'Mild Demented', '2024-10-28 13:32:20'),
(3, 5, 'static/tests/mild_118.jpg', 'Mild Demented', '2024-10-28 15:56:00'),
(4, 3, 'static/tests/moderate_3.jpg', 'Moderate Demented', '2024-10-28 16:00:40'),
(5, 3, 'static/tests/non_1011.jpg', 'Non Demented', '2024-10-28 16:00:58'),
(6, 1, 'static/tests/non_1004.jpg', 'Non Demented', '2024-10-28 16:12:24');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `username` varchar(50) NOT NULL,
  `email` varchar(100) NOT NULL,
  `password` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `username`, `email`, `password`) VALUES
(1, 'ss', 'ss@gmail.com', 'ss'),
(3, 'sajjad', 'sajjad@gmail.com', '123'),
(5, 'abc', 'abc@gmail.com', 'abc');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `prediction_history`
--
ALTER TABLE `prediction_history`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_id` (`user_id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`),
  ADD UNIQUE KEY `email` (`email`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `prediction_history`
--
ALTER TABLE `prediction_history`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `prediction_history`
--
ALTER TABLE `prediction_history`
  ADD CONSTRAINT `prediction_history_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
