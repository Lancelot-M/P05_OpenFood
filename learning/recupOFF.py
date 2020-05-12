#!/usr/bin/env python

import mysql.connector
from mysql.connector import Error

def create_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
                host = host_name,
                user = user_name,
                passwd = user_password,
                database = db_name
        )
        print("Connection to MYSQL DB successful")
    except Error as e:
        print("The error",{e}, "occurred")

    return connection

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully POUET")
    except Error as e:
        print("The error", e, "occurred")

def execute_fillquery(connection, query, value):
    cursor = connection.cursor()
    try:
        cursor.executemany(query, value)
        connection.commit()
        print("Query executed successfully BANANA")
    except Error as e:
        print("The error", e, "occured")

def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print("The error", e, "occurred")

delete_comment = "DROP TABLE IF EXISTS categorie;"

create_categorie_table = """
CREATE TABLE IF NOT EXISTS categorie (
    id SMALLINT AUTO_INCREMENT,
    name VARCHAR(40) NOT NULL,
    url TEXT,
    products INT,
    PRIMARY KEY (id)
) ENGINE=InnoDB;
"""

insert_categorie = """
INSERT INTO categorie (
    name, url, products)
VALUES
    (%s, %s, %s);
"""

select_cat = "SELECT * FROM categorie;"

categorie1 = [("Bolognese lasagne", "url-bidon.com", 69),
                ("Tarte", "uuuu", 0)]


connection = create_connection("localhost", "lancelot", "mdp", "OpenFoodFact")
execute_query(connection, delete_comment)
execute_query(connection, create_categorie_table)
execute_fillquery(connection, insert_categorie, categorie1)
categorie = execute_read_query(connection, select_cat)

for el in categorie:
    print("---")
    print(el)
