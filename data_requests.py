from db_connection import Base_fn
from constantes import CATEGORIES, MAX_PROD

class CategoriesRequests:
    """Interface with database."""

    def create_table(db):
        """Create the categories table."""
        
        query = """
        CREATE TABLE IF NOT EXISTS categories (
            id SMALLINT AUTO_INCREMENT,
            name VARCHAR(40) NOT NULL,
            url TEXT,
            products INT,
            PRIMARY KEY (id)
        ) ENGINE=InnoDB;
        """
        Base_fn.execute_query(db, query)

    def add_data(db, data_dict):
        """Insert value in table."""

        query = """
        INSERT INTO categories (
            id, name, url, products)
        VALUES
            (%s, %s, %s, %s);
        """
        for value in data_dict.values():
            data = (value.id_bdd, value.name, value.url, value.products)
            Base_fn.execute_query(db, query, data)

    def get_data(db, data):
        """Return the name of each categorie."""

        b_query = """SELECT {} FROM categories;"""
        query = b_query.format(data)
        result = Base_fn.select_query(db, query)
        result_filter = []
        for element in result:
            result_filter.append(element[0])
        return result_filter

    def del_table(db):
        """Delete table."""

        query = """DROP TABLE IF EXISTS categories;"""
        Base_fn.execute_query(db, query)

class AlimentsRequests:
    """Interface with Aliments Table."""

    def create_table(db):
        """Create table Aliments."""

        query = """
        CREATE TABLE IF NOT EXISTS aliments (
            product_name VARCHAR(200),
            id_off BIGINT,
            store VARCHAR(40),
            nutrition_grade VARCHAR(5),
            categorie TEXT
            ) ENGINE=InnoDB;
            """
        Base_fn.execute_query(db, query)

    def add_data(db, data_list):
        """Initialize aliments table."""

        query = """
        INSERT INTO aliments (
            store, product_name, categorie, nutrition_grade, id_off)
        VALUES (
            %s, %s, %s, %s, %s);
        """
        for element in data_list:
            data_aliment = (element.stores, element.product_name, element.categorie, element.nutrition_grades,
                                element.id_off)
            Base_fn.execute_query(db, query, data_aliment)

    def get_data(db, data):
        """Return data from aliments table."""

        b_query = """SELECT {} FROM aliments;"""
        query = b_query.format(data)
        result = Base_fn.select_query(db, query)
        result_filter = []
        for element in result:
            result_filter.append(element[0])
        return result_filter


    def get_aliments_by_category(db, category):
        """Return aliments by a categorie."""

        b_query = """SELECT product_name FROM aliments WHERE categorie='{}';"""
        query = b_query.format(category)
        result = Base_fn.select_query(db, query)
        result_filter = []
        for element in result:
            result_filter.append(element[0])
        return result_filter

    def substitute_aliment(db, category):
        """Return a list of MAX_PROD healthier aliments."""

        b_query = """
        SELECT 
            product_name
        FROM
            aliments
        WHERE
            categorie='{}'
        ORDER BY
            nutrition_grade;
        """
        query = b_query.format(category)
        result = Base_fn.select_query(db, query)
        result = result[0 : MAX_PROD]
        result_filter = []
        for element in result:
            result_filter.append(element[0])
        return result_filter

    def del_table(db):
        """Delete table."""

        query = """DROP TABLE IF EXISTS aliments ;"""
        Base_fn.execute_query(db, query)

class SavesRequests:
    """Interface with Saves Table."""

