from speedyserv.config.mysqlconnection import connectToMySQL
from speedyserv import DB

#from speedyserv.models import meal_model

class Category:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def add_category(cls, data):
        query = "INSERT INTO categories (name) VALUES (%(name)s)"
        return connectToMySQL(DB).query_db(query, data)
    
    @classmethod
    def get_all_categories(cls):
        query= """
                SELECT * FROM categories;
                """
        result =  connectToMySQL(DB).query_db(query)
        all_categories = []
        for cat in result:
            all_categories.append(cls(cat))
        return all_categories
    
    @classmethod
    def get_category_by_id(cls, data):
        query= """
                SELECT * FROM categories
                WHERE id = %(id)s
                """
        result =  connectToMySQL(DB).query_db(query, data)
        return cls(result[0])
    
    # @classmethod
    # def get_categories_with_meals(cls):
    #     query= """
    #             SELECT * FROM categories
    #             RIGHT JOIN meals ON categories.id = meals.category_id
    #             """
    #     result =  connectToMySQL(DB).query_db(query)
    #     all_categories = []
    #     for cat in result:
    #         all_categories.append(cls(cat))
    #     for row in result:
    #         meal = {
    #             'id': row['meals.id'],
    #             'name': row['meals.name'],
    #             'description': row['description'],
    #             'created_at': row['meals.created_at'],
    #             'updated_at': row['meals.updated_at'],
    #             'category_id': row['category_id'],
    #             'price': row['price']
    #         }

    #         cls.meals.append(meal_model.Meal(meal))
    #         print
        
    #     return all_categories

