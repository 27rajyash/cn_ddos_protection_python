#!/bin/bash
# Remember to type in your own root password for both your system and mysqlserver before executing the file.

# Exit immediately if a command exits with a non-zero status
set -e

# Step 1: Install Homebrew if it isn't installed
if ! command -v brew &> /dev/null
then
    echo "Homebrew not found. Installing Homebrew..."
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
else
    echo "Homebrew is already installed."
fi

# Step 2: Install MySQL (or MariaDB) using Homebrew
echo "Installing MySQL..."
brew install mysql

# Step 3: Start MySQL service and ensure it starts on boot
echo "Starting MySQL service..."
brew services start mysql

# Step 4: Secure MySQL installation
echo "Securing MySQL installation..."
mysql_secure_installation <<EOF

y
your_root_password # ==MAKE A CHANGE HERE!!! This is your system root password==
y
y
y
y
EOF

# Step 5: Create a new MySQL user and database
echo "Creating database and user..."
MYSQL_ROOT_PASSWORD="your_root_password" # ==MAKE A CHANGE HERE!!! This is your mysqlserver root password==
MYSQL_USER="ddos_user"
MYSQL_DB="ddos_webserver"
MYSQL_PASSWORD="ddos"

# SQL file to initialize the database
SQL_FILE="ddos_database.sql"

if [ ! -f "$SQL_FILE" ]; then
    echo "SQL file $SQL_FILE not found in the current directory!"
    exit 1
fi


# Login to MySQL and execute commands to create user and database
mysql -u root -p${MYSQL_ROOT_PASSWORD} <<EOF
CREATE DATABASE IF NOT EXISTS ${MYSQL_DB};
CREATE USER '${MYSQL_USER}'@'localhost' IDENTIFIED BY '${MYSQL_PASSWORD}';
GRANT ALL PRIVILEGES ON ${MYSQL_DB}.* TO '${MYSQL_USER}'@'localhost';
FLUSH PRIVILEGES;
SOURCE $(realpath ${SQL_FILE});
EXIT;
EOF

# Step 6: Verify if MySQL user and database were created successfully
echo "Verifying MySQL user and database creation..."
mysql -u ${MYSQL_USER} -p${MYSQL_PASSWORD} -e "SHOW DATABASES;"

echo "MySQL setup completed successfully!"