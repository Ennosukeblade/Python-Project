from speedyserv.config.mysqlconnection import connectToMySQL
from speedyserv import DB

from speedyserv.models import category_model

class Meal:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.price = data['price']
        self.description = data['description']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.category_id = data['category_id']
        self.category = category_model.Category.get_category_by_id({'id': self.category_id}).name

    @classmethod
    def get_all_meals(cls):
        query= """
                SELECT * FROM meals;
                """
        result =  connectToMySQL(DB).query_db(query)
        all_meals = []
        for meal in result:
            all_meals.append(cls(meal))
        return all_meals