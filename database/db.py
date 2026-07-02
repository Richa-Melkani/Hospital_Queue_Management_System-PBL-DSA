import mysql.connector
from mysql.connector import Error


def get_connection():
    try:

        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1234",
            database="hospital_queue_db",
            autocommit=False
        )

        return connection

    except Error as e:

        print(f"Database Connection Error: {e}")

        return None