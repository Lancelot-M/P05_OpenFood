import mysql.connector
from mysql.connector import Error

class CategoriesRequests:
    """Interface with database."""

    def execute_query(connection, query):
        """Send instruction to db."""

        cursor = connection.cursor()
        try:
            cursor.execute(query)
            connection.commit()
            print("Query executed successfully")
        except Error as e:
            print("The error", e, "occured")

    def create_table(db):
        """Create the categorie table."""
        
        query = """
        CREATE TABLE IF NOT EXISTS categorie (
            id SMALLINT AUTO_INCREMENT,
            name VARCHAR(40) NOT NULL,
            url TEXT,
            products INT,
            PRIMARY KEY (id)
        ) ENGINE=InnoDB;
        """
        execute_query(db, query)

    def add_data(db, value):
        """Insert value in table."""

        query = """
        INSERT INTO categorie (
            name, url, products)
        VALUES
            (%s, %s, %s);
        """
        execute_query(db, query)

    def del_table(db):
        """Delete table."""

        query = """DROP TABLE IF EXISTS categorie;"""
        execute_query(db)

class AlimentsRequests:
    """Interface with Aliments Table."""

class SavesRequests:
    """Interface with Saves Table."""

