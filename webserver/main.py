from flask import Flask, request, jsonify
import mysql.connector
from mysql.connector import Error
import hashlib

web = Flask(__name__)

# MySQL database credentials
MYSQL_HOST = 'localhost'
MYSQL_DATABASE = 'ddos_webserver'
MYSQL_USER = 'ddos_user'
MYSQL_PASSWORD = 'ddos'


@web.route('/', methods=['GET'])
def home():
    return "This is a test server for our DDoS protection application."


def heavy_computation():
    for _ in range(10**6):
        hashlib.sha256(b"Attack simulation").hexdigest()


@web.route('/computational-task', methods=['GET'])
def heavy_task():
    heavy_computation()
    return f"Heavy work has been completed!", 200


# Function to create a MySQL connection
def create_connection():
    try:
        connection = mysql.connector.connect(
            host=MYSQL_HOST,
            database=MYSQL_DATABASE,
            user=MYSQL_USER,
            password=MYSQL_PASSWORD
        )
        if connection.is_connected():
            print("Connected to MySQL database")
            return connection
    except Error as e:
        print("Error while connecting to MySQL", e)
    return None


# This function will create the database from ./ddos_database.sql.
def create_database():
    pass


# Route to insert data into MySQL
@web.route('/add-task', methods=['POST'])
def add_task():
    connection = create_connection()
    if connection is not None:
        cursor = connection.cursor()
        task_name = request.json.get('task_name')
        task_description = request.json.get('task_description')

        # SQL query to insert a task into the database
        query = "INSERT INTO tasks (task_name, task_description) VALUES (%s, %s)"
        cursor.execute(query, (task_name, task_description))
        connection.commit()
        cursor.close()
        connection.close()
        return jsonify({"message": "Task added successfully!"}), 201
    return jsonify({"message": "Failed to connect to the database."}), 500


# Route to fetch tasks from MySQL
@web.route('/tasks', methods=['GET'])
def get_tasks():
    connection = create_connection()
    if connection is not None:
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM tasks")
        tasks = cursor.fetchall()
        cursor.close()
        connection.close()
        return jsonify(tasks), 200
    return jsonify({"message": "Failed to connect to the database."}), 500