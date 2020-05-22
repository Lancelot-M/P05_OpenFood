import mysql.connector
from mysql.connector import Error

class Base_fn:
    """Mysql heart function."""
    
    def create_connection(host_name, user_name, user_password, db_name):
        """Connection to database."""

        connection = None
        try:
            connection = mysql.connector.connect(
                    host=host_name,
                    user=user_name,
                    passwd=user_password,
                    database=db_name)
            print("Connection to MYSQL DB successful.")
        except Error as e:
            print("The error", e, "occured.")
        return connection

    def execute_query(connection, query, value=None):
        """For Drop, Create, Insert query."""
    
        cursor = connection.cursor()
        try:
            cursor.execute(query, value)
            connection.commit()
            print("Query executed successfully.")
        except Error as e:
            print("The error", e, "occured")

    def select_query(connection, query):
        """For Select query."""

        cursor = connection.cursor()
        result = None
        try:
            cursor.execute(query)
            result = cursor.fetchall()
            #print("Select query executed successfully.")
            return result
        except Error as e:
            print("The error", e, "occured")
