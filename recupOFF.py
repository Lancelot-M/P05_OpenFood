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
        print("Query executed successfully")
    except Error as e:
        print("The error", e, "occurred")


delete_comment = "DELETE FROM categorie"

create_categorie_table = """
CREATE TABLE IF NOT EXISTS categorie (
    id INT,
    name VARCHAR(40) NOT NULL,
    description TEXT,
    PRIMARY KEY (name)
) ENGINE=InnoDB
"""


create_cat = """
INSERT INTO
    categorie (id, name, description)
VALUES
    (13948, 'cereales', 'produits issus des grosses moissnoneuz'),
    (3, 'laitages', NULL),
    (4930, 'plomb', 'peinture indigeste');
"""


def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print("The error", e, "occurred")

select_cat = "SELECT * FROM categorie"


connection = create_connection("localhost", "lancelot", "mdp", "OpenFoodFact")
execute_query(connection, delete_comment)
execute_query(connection, create_categorie_table)
execute_query(connection, create_cat)
categorie = execute_read_query(connection, select_cat)
for cat in categorie:
    print(cat)
