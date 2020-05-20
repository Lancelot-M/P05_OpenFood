from System.Requests.db_connection import Base_fn

class CategoriesRequests:
    """Interface with database."""

    def create_table(db):
        """Create the categories table."""

        query = """
        CREATE TABLE IF NOT EXISTS categories (
            id SMALLINT AUTO_INCREMENT,
            name VARCHAR(50) NOT NULL,
            url TEXT,
            products INT,
            PRIMARY KEY (id),
            INDEX index_nam (name)
        ) ENGINE=InnoDB;
        """
        Base_fn.execute_query(db, query)

    def add_data(db, data_dict):
        """Insert value in table."""

        query = """
        INSERT INTO categories (
            name, url, products)
        VALUES
            (%s, %s, %s);
        """
        for value in data_dict.values():
            data = (value.name, value.url, value.products)
            Base_fn.execute_query(db, query, data)

    def get_data(db, data):
        """Return the column=data in categories."""

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
