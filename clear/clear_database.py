#This is an unnecessary file to remove all the test tasks appended during the attack from the database.

import mysql.connector
import hashlib
from mysql.connector import Error

# MySQL database credentials
MYSQL_HOST = 'localhost'
MYSQL_DATABASE = 'ddos_webserver'
MYSQL_USER = 'ddos_user'
MYSQL_PASSWORD = 'ddos'

def remove_excess():
    try:
        connection = mysql.connector.connect(
            host=MYSQL_HOST,
            database=MYSQL_DATABASE,
            user=MYSQL_USER,
            password=MYSQL_PASSWORD
        )
        if connection.is_connected():
            cursor = connection.cursor()
            
            query = "DELETE FROM tasks WHERE task_name = 'Test Task'"
            cursor.execute(query)

            query = "ALTER TABLE tasks AUTO_INCREMENT = 3"
            cursor.execute(query)

            connection.commit()
            cursor.close()
            connection.close()
            print("Remove all the unnecessary tasks from tasks table of database 'ddos_webserver'.")
    
    except Error as e:
        print("Error while connecting to MySQL:", e)

    return None

remove_excess()