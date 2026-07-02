from flask import Flask, render_template, request, redirect, url_for,flash
from database.db import get_connection
from algorithms.priority_queue import Patient, PriorityQueue
from algorithms.round_robin import RoundRobinScheduler
from algorithms.stack_history import TreatmentHistory

app = Flask(__name__)
app.secret_key = "hospital_queue_secret_key"

# -----------------------------
# Initialize Data Structures
# -----------------------------
patient_queue = PriorityQueue()
doctor_scheduler = RoundRobinScheduler()
treatment_history = TreatmentHistory()


# -----------------------------
# Load Waiting Patients From Database
# -----------------------------
def load_patients():

    connection = get_connection()

    if connection is None:
        return

    cursor = connection.cursor(dictionary=True)

    cursor.execute("""
        SELECT *
        FROM patients
        WHERE status='Waiting'
        ORDER BY patient_id
    """)

    rows = cursor.fetchall()

    cursor.close()
    connection.close()

    patient_queue.clear()

    for row in rows:

        patient = Patient(
            row["patient_id"],
            row["name"],
            row["age"],
            row["disease"],
            row["severity"]
        )

        patient_queue.add_patient(patient)


# -----------------------------
# Home Page
# -----------------------------
@app.route("/")
def home():

    load_patients()

    connection = get_connection()

    total_patients = 0
    waiting_patients = 0
    treated_patients = 0

    if connection:

        cursor = connection.cursor(dictionary=True)

        cursor.execute("SELECT COUNT(*) AS total FROM patients")
        total_patients = cursor.fetchone()["total"]

        cursor.execute("SELECT COUNT(*) AS waiting FROM patients WHERE status='Waiting'")
        waiting_patients = cursor.fetchone()["waiting"]

        cursor.execute("SELECT COUNT(*) AS treated FROM patients WHERE status='Treated'")
        treated_patients = cursor.fetchone()["treated"]

        cursor.close()
        connection.close()

    return render_template(
        "index.html",
        total_patients=total_patients,
        waiting_patients=waiting_patients,
        treated_patients=treated_patients
    )


# -----------------------------
# Add Patient
# -----------------------------
@app.route("/add_patient", methods=["GET", "POST"])
def add_patient():

    if request.method == "POST":

        name = request.form["name"]
        age = int(request.form["age"])
        disease = request.form["disease"]
        severity = int(request.form["severity"])

        connection = get_connection()

        if connection:

            cursor = connection.cursor()

            cursor.execute("""
                INSERT INTO patients
                (name, age, disease, severity)
                VALUES (%s,%s,%s,%s)
            """, (name, age, disease, severity))

            connection.commit()

            patient_id = cursor.lastrowid

            cursor.close()
            connection.close()

            patient = Patient(
                patient_id,
                name,
                age,
                disease,
                severity
            )

            patient_queue.add_patient(patient)
            flash("Patient added successfully!", "success")

        return redirect(url_for("queue"))

    return render_template("add_patient.html")


# -----------------------------
# Display Queue
# -----------------------------
@app.route("/queue")
def queue():

    load_patients()

    patients = patient_queue.get_all_patients()

    return render_template(
        "queue.html",
        patients=patients
    )

# -----------------------------
# Search Patient
# -----------------------------
@app.route("/search", methods=["GET", "POST"])
def search():

    patient = None

    if request.method == "POST":

        patient_id =int(request.form["patient_id"])

        connection = get_connection()

        if connection:

            cursor = connection.cursor(dictionary=True)

            cursor.execute(
                "SELECT * FROM patients WHERE patient_id=%s",
                (patient_id,)
            )

            patient = cursor.fetchone()
            if not patient:
                flash("Patient not found!", "danger")

            cursor.close()
            connection.close()

    return render_template(
        "search.html",
        patient=patient
    )


# -----------------------------
# Treat Patient
# -----------------------------
@app.route("/treat")
def treat():

    load_patients()

    if patient_queue.is_empty():
        flash("No patients available in the queue!", "warning")
        return redirect(url_for("queue"))

    patient = patient_queue.treat_patient()

    doctor = doctor_scheduler.assign_doctor()

    connection = get_connection()

    if connection:

        cursor = connection.cursor()

        # Update patient status
        cursor.execute("""
            UPDATE patients
            SET status='Treated',
                assigned_doctor=%s
            WHERE patient_id=%s
        """, (doctor, patient.patient_id))

        # Save treatment history
        cursor.execute("""
            INSERT INTO treatment_history
            (patient_id, doctor_name)
            VALUES (%s,%s)
        """, (patient.patient_id, doctor))

        connection.commit()

        cursor.close()
        connection.close()

    treatment_history.add_record(patient)
    flash("Patient treated successfully!", "success")

    return render_template(
        "treat.html",
        patient=patient,
        doctor=doctor
    )


# -----------------------------
# Treatment History
# -----------------------------
@app.route("/history")
def history():

    connection = get_connection()

    history = []

    if connection:

        cursor = connection.cursor(dictionary=True)

        cursor.execute("""
            SELECT
                t.history_id,
                p.patient_id,
                p.name,
                p.disease,
                t.doctor_name,
                t.treatment_time
            FROM treatment_history t
            JOIN patients p
            ON t.patient_id = p.patient_id
            ORDER BY t.treatment_time DESC
        """)

        history = cursor.fetchall()

        cursor.close()
        connection.close()

    return render_template(
        "history.html",
        history=history
    )


# -----------------------------
# Run Application
# -----------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
