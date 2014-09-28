from flask import Flask
from flask.ext.restful import Api
from flask.ext.mongoengine import MongoEngine
from flask.ext.login import LoginManager

app=Flask(__name__)
api=Api(app)
login_manager=LoginManager()
login_manager.init_app(app)
app.config["MONGODB_SETTINGS"] = {'DB': "test_database"}
app.config["SECRET_KEY"] = "qwertyuiop"

db = MongoEngine(app)
# # app.config.from_object('config')

# # from app import views, models
