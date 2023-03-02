from speedyserv.config.mysqlconnection import connectToMySQL
from speedyserv import DB

class Order:
    def __init__(self,data):
        self.id = data['id']
        self.table_id = data['table_id']
        self.meal_id = data['meal_id']

    # @classmethod
    # def create_order(cls,data):
    #     query = "INSERT INTO orders (table_id) VALUES (%(table_id)s)"
    #     return connectToMySQL(DB).query_db(query, data)

    @classmethod
    def create_order(cls,data):
        query = "INSERT INTO orders (meal_id, table_id) VALUES (%(meal_id)s, %(table_id)s)"
        return connectToMySQL(DB).query_db(query, data)