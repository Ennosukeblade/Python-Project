from speedyserv.config.mysqlconnection import connectToMySQL
from speedyserv import DB

class Table:
    def __init__(self, data):
        self.id = data['id']
        self.status = data['status'] or 0
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.meals = []

    @classmethod
    def get_all_tables(cls):
        query= """
                SELECT * FROM tables;
                """
        result =  connectToMySQL(DB).query_db(query)
        all_tables = []
        for table in result:
            all_tables.append(cls(table))
        return all_tables
    
    @classmethod
    def add_table(cls, data):
        query = """
                INSERT INTO tables (id)
                VALUES (%(id)s)
                """
        return connectToMySQL(DB).query_db(query, data)
    
    @classmethod
    def delete_table(cls, data):
        query = "DELETE FROM tables WHERE id = %(id)s;"
        return connectToMySQL(DB).query_db(query, data)
    
    @classmethod
    def update_table_status(cls, data):
        query = """
                UPDATE tables SET
                status = %(status)s
                WHERE id = %(id)s
                """
        return connectToMySQL(DB).query_db(query, data)

    @classmethod
    def get_meals_with_table_id(cls, data):
        query = """
                SELECT * FROM tables
                LEFT JOIN orders ON tables.id = orders.table_id
                LEFT JOIN meals ON meals.id=orders.meal_id
                WHERE tables.id =  %(id)s;
                """
        result =  connectToMySQL(DB).query_db(query, data)
        table = cls(result[0])
        for row in result:
            meals


        print(result)
        return []