# 🏥 Hospital Queue Management System (C++)

A console-based Hospital Queue Management System built using C++. This project simulates real-world hospital patient management using priority queue, stack, and dynamic scheduling logic.

---

## 📌 Features

- Add normal patients with severity levels  
- Add emergency patients with highest priority automatically  
- Automatic doctor assignment (round-robin system)  
- Priority-based patient treatment system  
- Search patient by ID  
- Display all patients in queue  
- Maintain patient treatment history using stack  
- Dynamic priority adjustment based on waiting time  

---

## 🧠 Core Concepts Used

- Priority Queue (Heap-based scheduling)  
- Stack (history tracking)  
- Struct-based data modeling  
- Greedy scheduling algorithm  
- Time-based priority adjustment  

---

## ⚙️ How It Works

### Patient Priority System
Each patient has:
- Severity:
  - 1 = Critical
  - 2 = Medium
  - 3 = Low

Priority increases when waiting time increases, ensuring fair scheduling.

### Emergency Handling
Emergency patients are automatically assigned highest priority and treated first.

### Doctor Assignment
Doctors are assigned in circular order:
Dr. Sharma → Dr. Mehta → Dr. Khan → Dr. Singh → repeat

---

## 🗂️ Project Structure
```
Hospital Queue Management System/
├──LICENSE
├── main.cpp
├── README.md
```
---

## ▶️ How to Run

Compile and run using g++:

g++ main.cpp -o hospital
./hospital

---

## 🖥️ Menu Options

1. Add Patient  
2. Add Emergency Patient  
3. Treat Patient  
4. Display Patients  
5. Search Patient  
6. Patient History  
7. Exit  

---

## 📊 Workflow

- Add patients to queue  
- System automatically assigns priority  
- Highest priority patient is treated first  
- Doctor is assigned automatically  
- Treated patients stored in history stack  
- Search and display available anytime  

---

## 🚀 Future Improvements

- GUI version using Qt or web app  
- Database integration (MySQL / SQLite)  
- Login system for staff  
- Real-time hospital dashboard  
- AI-based triage system  

---

## 👩‍💻 Author

**Richa Melkani** 

---

## 📜 License

For educational purposes only
