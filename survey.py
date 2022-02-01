from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import flash

class Survey:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.language = data['language']
        self.comments = data['comments']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls,data):
        query = "INSERT into surveys (name,location,language,comments) VALUES (%(name)s,%(location)s,%(language)s,%(comments)s);"
        return connectToMySQL('dojo_survey').query_db(query,data)

    @classmethod
    def get_last_survey(cls):
        query = "SELECT * FROM surveys ORDER BY surveys.id DESC LIMIT 1;"
        results = connectToMySQL('dojo_survey').query_db(query)
        return Survey(results[0])

    @staticmethod
    def is_valid(survey):
        is_valid = True
        if len(survey['name']) < 3:
            is_valid = False
            flash("Name must be at least 3 characters.")
        if len(survey['location']) < 1:
            is_valid = False
            flash("Must choose a dojo location.")
        if len(survey['language']) < 1:
            is_valid = False
            flash("Must choose a favorite language.")
        if len(survey['comments']) < 3:
            is_valid = False
            flash("Comments must be at least 3 characters.")
        return is_valid