# Hospital_Queue_Management_System-PBL-
Priority-based hospital queue system using C++

Overview

The Hospital Queue Management System is a C++ console-based application that manages patient treatment using a priority-based scheduling approach instead of the traditional first-come-first-served system.

The system ensures that critical patients are treated first, while also considering waiting time, making it more fair and realistic for hospital scenarios.

🚀 Features
✅ Add regular patients
🚨 Add emergency patients (auto high priority)
⚡ Priority-based patient treatment using priority_queue
⏳ Dynamic priority adjustment based on waiting time
👨‍⚕️ Doctor assignment using round-robin scheduling
🔍 Search patient by ID
📜 View last treated patient (history using stack)
📋 Display all patients in queue
🖥️ Menu-driven user interface
🛠️ Technologies Used
Language: C++
Concepts Used:
STL (priority_queue, stack, vector)
Structures (struct)
Custom Comparator
Queue Scheduling Algorithms
Basic OOP concepts
🧠 Core Logic
🔹 Priority Calculation

Patient priority is determined using:

effective_severity = severity - (waiting_time / 5)
Lower value = Higher priority
Minimum severity is clamped to 1
Waiting time increases priority over time
🔹 Data Structures Used
Data Structure	Purpose
priority_queue	Manage patients based on priority
stack	Store treatment history
vector	Store doctor list
struct Patient	Store patient details
👨‍⚕️ Doctor Assignment

Doctors are assigned using Round Robin Scheduling:

Dr. Sharma → Dr. Mehta → Dr. Khan → Dr. Singh → repeat
📂 Project Structure
hospital-queue-management-system/
│── main.cpp
│── README.md
▶️ How to Run
Step 1: Compile
g++ main.cpp -o hospital_queue
Step 2: Run
./hospital_queue
📋 Menu Options
1. Add Patient
2. Add Emergency Patient
3. Treat Patient
4. Display Patients
5. Search Patient
6. Patient History
7. Exit
⚠️ Limitations
Single-file implementation
No database (data resets after program ends)
Limited input handling (no multi-word names)
🔮 Future Enhancements
GUI-based interface
Database integration (MySQL / MongoDB)
Multi-doctor parallel treatment
Patient record persistence
Online appointment system
Conclusion

This project demonstrates how data structures and algorithms can be applied to solve real-world problems like hospital management. It improves efficiency, fairness, and prioritization in patient treatment.
