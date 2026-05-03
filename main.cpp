#include <iostream>
#include <queue>
#include <stack>
#include <vector>
using namespace std;

//PATIENT
struct Patient {
    int id;
    string name;
    int age;
    string disease;
    int severity;
    int arrivalTime;

    Patient(int i, string n, int a, string d, int s, int t) {
        id = i;
        name = n;
        age = a;
        disease = d;
        severity = s;
        arrivalTime = t;
    }
};

//DOCTORS
vector<string> doctors = {
    "Dr. Sharma",
    "Dr. Mehta",
    "Dr. Khan",
    "Dr. Singh"
};

int doctorIndex = 0;

//GLOBAl
int currentTime = 0;
int patientID = 1;

//COMPARATOR
struct Compare {
    bool operator()(Patient const& p1, Patient const& p2) {

        int wait1 = currentTime - p1.arrivalTime;
        int wait2 = currentTime - p2.arrivalTime;

        int effective1 = p1.severity - (wait1 / 5);
        int effective2 = p2.severity - (wait2 / 5);

        if (effective1 < 1) effective1 = 1;
        if (effective2 < 1) effective2 = 1;

        if (effective1 == effective2)
            return p1.arrivalTime > p2.arrivalTime;

        return effective1 > effective2;
    }
};

//DATA STRUCTURES
priority_queue<Patient, vector<Patient>, Compare> pq;
stack<Patient> history;

//UPDATE
void updatePriorities() {
    vector<Patient> temp;

    while (!pq.empty()) {
        temp.push_back(pq.top());
        pq.pop();
    }

    for (auto &p : temp) {
        pq.push(p);
    }
}

int main() {

    int choice;

    do {
        cout << "\nHospital Queue Management System\n";
        cout << "1. Add Patient\n";
        cout << "2. Add Emergency Patient\n";
        cout << "3. Treat Patient\n";
        cout << "4. Display Patients\n";
        cout << "5. Search Patient\n";
        cout << "6. Patient History\n";
        cout << "7. Exit\n";
        cout << "Enter choice: ";
        cin >> choice;

        switch (choice) {

        case 1:
        case 2: {
            string name, disease;
            int age, severity;

            cout << "Enter Name: ";
            cin >> name;

            cout << "Enter Age: ";
            cin >> age;

            cout << "Enter Disease: ";
            cin >> disease;

            if (choice == 2) {
                severity = 1;
                cout << "Emergency patient added!\n";
            } else {
                cout << "Enter Severity (1-Critical, 2-Medium, 3-Low): ";
                cin >> severity;
            }

            Patient p(patientID++, name, age, disease, severity, currentTime++);
            pq.push(p);

            cout << "Patient added with ID: " << p.id << endl;
            break;
        }

        case 3: {
            if (pq.empty()) {
                cout << "No patients to treat.\n";
                break;
            }

            updatePriorities();

            Patient p = pq.top();
            pq.pop();

            string assignedDoctor = doctors[doctorIndex];
            doctorIndex = (doctorIndex + 1) % doctors.size();

            cout << "\nTreating Patient:\n";
            cout << "ID: " << p.id << ", Name: " << p.name << endl;
            cout << "Disease: " << p.disease << endl;
            cout << "Assigned Doctor: " << assignedDoctor << endl;

            history.push(p);
            break;
        }

        case 4: {
            if (pq.empty()) {
                cout << "No patients in queue.\n";
                break;
            }

            updatePriorities();

            priority_queue<Patient, vector<Patient>, Compare> temp = pq;

            cout << "\nPatients in Queue:\n";
            while (!temp.empty()) {
                Patient p = temp.top();
                temp.pop();

                cout << "ID: " << p.id
                     << ", Name: " << p.name
                     << ", Severity: " << p.severity
                     << ", Disease: " << p.disease << endl;
            }
            break;
        }

        case 5: {
            int id;
            cout << "Enter Patient ID: ";
            cin >> id;

            priority_queue<Patient, vector<Patient>, Compare> temp = pq;
            bool found = false;

            while (!temp.empty()) {
                Patient p = temp.top();
                temp.pop();

                if (p.id == id) {
                    cout << "Patient Found:\n";
                    cout << "Name: " << p.name << ", Disease: " << p.disease << endl;
                    found = true;
                    break;
                }
            }

            if (!found) cout << "Patient not found.\n";
            break;
        }

        case 6: {
            if (history.empty()) {
                cout << "No treatment history.\n";
            } else {
                Patient p = history.top();
                cout << "Last Treated Patient:\n";
                cout << "ID: " << p.id << ", Name: " << p.name << endl;
            }
            break;
        }

        case 7:
            cout << "Exiting\n";
            break;

        default:
            cout << "Invalid choice!\n";
        }

    } while (choice != 7);

    return 0;
}
