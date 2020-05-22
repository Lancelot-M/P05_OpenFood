"""File who contain SaveRequests object."""

from System.Requests.db_connection import Base_fn

class SaveRequests:
    """Interface with Save Table."""

    def create_table(db):
        """Create table save."""
        query = """
        CREATE TABLE IF NOT EXISTS save (
        product_choose VARCHAR(200) NOT NULL,
        substitut_choose VARCHAR(200) NOT NULL,
        FOREIGN KEY (product_choose) REFERENCES aliments(product_name),
        FOREIGN KEY (substitut_choose) REFERENCES aliments(product_name)
        ) ENGINE=InnoDB;
        """
        Base_fn.execute_query(db, query)

    def add_data(db, data):
        """Add a data to table save."""
        query = """INSERT INTO save VALUES (%s, %s);"""
        Base_fn.execute_query(db, query, data)

    def get_all(db):
        """Select all table save."""
        query = """SELECT save.substitut_choose, save.product_choose, aliments.store, aliments.url
        FROM aliments
        INNER JOIN save
            ON aliments.product_name = save.product_choose;"""
        result = Base_fn.select_query(db, query)
        return result

    def del_table(db):
        """Delete save table."""
        query = """DROP TABLE IF EXISTS save;"""
        Base_fn.execute_query(db, query)
