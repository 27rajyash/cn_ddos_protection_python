from flask import Flask, request, jsonify
from database import create_connection, heavy_computation
from rate_limiter import log_request, limit_rate
# from flask_limiter import Limiter
# from flask_limiter.util import get_remote_address

web = Flask(__name__)
# limiter = Limiter(get_remote_address, app=web, default_limits=["200 per minute"])


@web.route('/', methods=['GET'])
def home():
    return "This is a test server for our DDoS protection application."


@web.route('/computational-task', methods=['GET'])
def heavy_task():
    heavy_computation()
    return f"Heavy work has been completed!", 200


# Route to insert data into MySQL
@web.route('/add-task', methods=['POST'])
@limit_rate(max_requests=100, window_size=60)
def add_task():
    connection = create_connection()
    if connection is not None:
        client_ip = request.remote_addr
        log_request(client_ip, "Method: Post - @web/add-task")

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
    
    else:
        return jsonify({"message": "Failed to connect to the database."}), 500


# Route to fetch tasks from MySQL
@web.route('/tasks', methods=['GET'])
@limit_rate(max_requests=100, window_size=60)
def get_tasks():
    connection = create_connection()
    if connection is not None:
        client_ip = request.remote_addr
        log_request(client_ip, "Method: GET - @web/tasks")

        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM tasks")
        tasks = cursor.fetchall()
        cursor.close()
        connection.close()
        return jsonify(tasks), 200
    
    else:
        return jsonify({"message": "Failed to connect to the database."}), 500


if __name__ == "__main__":
    web.run(debug=True, host='0.0.0.0', port=8000, threaded=True) 