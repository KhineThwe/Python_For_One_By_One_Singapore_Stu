import mysql.connector

config = {
    'user': 'root',
    'password': 'toor',
    'host': 'localhost',
    'database': 'onlinedb',
    'auth_plugin': 'mysql_native_password'
}

connection = mysql.connector.connect(**config)
print(connection)