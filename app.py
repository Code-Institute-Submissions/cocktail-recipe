import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo 
from bson.objectid import ObjectId

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'cookbook-data'
app.config["MONGO_URI"] = 'mongodb://cocktail-root:Forzaaudia1@ds125352.mlab.com:25352/cookbook-data'

mongo = PyMongo(app)

@app.route('/')
@app.route('/get_recipes')
def get_recipes():
    return render_template("recipes.html", 
    recipes=mongo.db.recipes.find())

# @app.route('/')
# def hello_test():
#     return "Hello World test"
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)


