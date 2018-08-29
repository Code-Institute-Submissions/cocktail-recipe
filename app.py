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
    recipes=mongo.db.recipes.find()
    return render_template("recipes.html", 
    recipes=recipes)

@app.route('/add_recipe')
def add_recipe():
    return render_template('addrecipe.html',
    difficulty=mongo.db.difficulty.find())

@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    recipes = mongo.db.recipes
    recipes.insert_one(request.form.to_dict())
    return redirect(url_for('get_recipes'))

@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    the_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template('editrecipe.html', recipes=the_recipe)


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)


