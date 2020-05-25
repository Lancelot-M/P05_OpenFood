"""File contain instruction for database."""

from System.Requests.db_connection import Base_fn
from System.System.constantes import MAX_PROD


class AlimentsRequests:
    """Methodes to interface with Aliments Table."""

    def create_table(db):
        """Create table aliments."""
        query = """
        CREATE TABLE IF NOT EXISTS aliments (
        product_name VARCHAR(200) NOT NULL,
        id_off BIGINT,
        url VARCHAR(200),
        store VARCHAR(40),
        nutrition_grades VARCHAR(5),
        categorie VARCHAR(50) NOT NULL,
        PRIMARY KEY (product_name)
        ) ENGINE=InnoDB;
        """
        Base_fn.execute_query(db, query)

    def add_data(db, data_list):
        """Initialize aliments table."""
        query = """
        INSERT INTO aliments (
            store, product_name, categorie, nutrition_grades, id_off, url)
        VALUES (
            %s, %s, %s, %s, %s, %s);
        """
        for element in data_list:
            data_aliment = (element.stores, element.product_name,
                            element.categorie, element.nutrition_grades,
                            element.id_off, element.url)
            Base_fn.execute_query(db, query, data_aliment)

    def get_data(db, data):
        """Return data from aliments table."""
        b_query = """SELECT {} FROM aliments."""
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
            product_name, store, url
        FROM
            aliments
        WHERE
            categorie='{}'
        ORDER BY
            nutrition_grades;
        """
        query = b_query.format(category)
        result = Base_fn.select_query(db, query)
        result = result[0: MAX_PROD]
        return result

    def del_table(db):
        """Delete table aliments."""
        query = """DROP TABLE IF EXISTS aliments;"""
        Base_fn.execute_query(db, query)
