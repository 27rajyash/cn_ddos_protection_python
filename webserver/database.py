import mysql.connector
import hashlib
from mysql.connector import Error

# MySQL database credentials
MYSQL_HOST = 'localhost'
MYSQL_DATABASE = 'ddos_webserver'
MYSQL_USER = 'ddos_user'
MYSQL_PASSWORD = 'ddos'

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


def heavy_computation():
    for _ in range(10**6):
        hashlib.sha256(b"Attack simulation").hexdigest()