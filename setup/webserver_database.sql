CREATE DATABASE ddos_webserver;

CREATE USER 'ddos_user'@'localhost' IDENTIFIED BY 'ddos';
GRANT ALL PRIVILEGES ON ddos_webserver.* TO 'ddos_user'@'localhost' WITH GRANT OPTION;

USE ddos_webserver;

DROP TABLE IF EXISTS tasks;
CREATE TABLE tasks (
    id INT AUTO_INCREMENT PRIMARY KEY,
    task_name VARCHAR(255) NOT NULL,
    task_description TEXT NOT NULL
);

INSERT INTO tasks (task_name, task_description) VALUES
('CN DDoS Project', 'Try to implement this Distributed Denial of Service Project with Rajjo within the next month.'),
('Professional level', 'Make it as close to real life including tests and automation scripts.');