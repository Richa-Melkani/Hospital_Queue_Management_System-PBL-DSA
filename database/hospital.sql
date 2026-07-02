-- Create Database
CREATE DATABASE IF NOT EXISTS hospital_queue_db;

USE hospital_queue_db;

-- -----------------------------
-- Patients Table
-- -----------------------------
CREATE TABLE patients (
    patient_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    age INT NOT NULL,
    disease VARCHAR(100) NOT NULL,
    severity INT NOT NULL CHECK (severity BETWEEN 1 AND 3),
    arrival_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    status ENUM('Waiting','Treated') DEFAULT 'Waiting',
    assigned_doctor VARCHAR(100) DEFAULT NULL
);

-- -----------------------------
-- Treatment History
-- -----------------------------
CREATE TABLE treatment_history (
    history_id INT AUTO_INCREMENT PRIMARY KEY,
    patient_id INT NOT NULL,
    doctor_name VARCHAR(100) NOT NULL,
    treatment_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (patient_id)
    REFERENCES patients(patient_id)
    ON DELETE CASCADE
);