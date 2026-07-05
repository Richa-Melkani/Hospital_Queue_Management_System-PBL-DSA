# 🏥 Hospital Queue Management System

A full-stack Hospital Queue Management System developed using **Python, Flask, MySQL, and Data Structures**.

The application manages patient registration, priority-based scheduling, doctor assignment, treatment workflow, and treatment history through an interactive web interface.

---

## 🚀 Live Demo

https://web-production-1f745.up.railway.app/

---

## 📸 Screenshots

### Home

![Home](screenshots/home.png)

### Add Patient

![Add Patient](screenshots/add_patient.png)

### Patient Queue

![Queue](screenshots/queue.png)

### Treatment

![Treatment](screenshots/treatment.png)

### History

![History](screenshots/history.png)

---

# Features

- Patient Registration
- Patient Search
- Priority-based Queue Management
- Automatic Doctor Assignment
- Treatment Workflow
- Treatment History
- Dynamic Priority Adjustment
- Responsive Dashboard
- Real-time Patient Statistics
- Railway Deployment

---

# Data Structures Used

## Priority Queue (Heap)

Patients are treated according to severity.

- Severity 1 → Critical
- Severity 2 → Medium
- Severity 3 → Low

Patients waiting longer automatically receive higher priority.

---

## Stack

Treatment history is maintained using Stack (LIFO).

- Add treated patient
- View latest treatment
- Maintain complete history

---

## Round Robin Scheduling

Doctors are assigned automatically in cyclic order.

Example:

Dr. Sharma

↓

Dr. Mehta

↓

Dr. Khan

↓

Dr. Singh

↓

Repeat

This ensures fair workload distribution.

---

# Tech Stack

## Backend

- Python
- Flask

## Database

- MySQL

## Frontend

- HTML5
- CSS3
- Bootstrap 5
- JavaScript

## Deployment

- Railway
- Gunicorn

---

# Project Structure

```
Hospital-Queue-Management-System/
│
├── app.py
├── requirements.txt
├── README.md
├── Procfile
│
├── algorithms/
│   ├── priority_queue.py
│   ├── round_robin.py
│   └── stack_history.py
│
├── database/
│   ├── db.py
│   └── hospital.sql
│
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── add_patient.html
│   ├── queue.html
│   ├── search.html
│   ├── treat.html
│   └── history.html
│
├── static/
│   ├── style.css
│   └── script.js
│
└── screenshots/
    ├── home.png
    ├── add_patient.png
    ├── queue.png
    ├── treatment.png
    └── history.png
```

---

# Installation

Clone the repository

```bash
git clone <github.com/Richa-Melkani/Hospital_Queue_Management_System-PBL-DSA>
```

Move into the project

```bash
cd Hospital-Queue-Management-System
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create MySQL database

```sql
SOURCE database/hospital.sql;
```

Update database credentials in

```
database/db.py
```

Run

```bash
python app.py
```

Open

```
http://127.0.0.1:5000
```

---

# Algorithms

### Priority Queue

- Heap-based implementation
- O(log n) insertion
- O(log n) deletion

### Stack

- O(1) push
- O(1) pop

### Round Robin

- O(1) doctor assignment

---

# Future Improvements

- User Authentication
- Admin Dashboard
- Email Notifications
- Appointment Booking
- PDF Reports
- Doctor Availability
- REST API
- Docker Support

---

# Author

**Richa Melkani**
