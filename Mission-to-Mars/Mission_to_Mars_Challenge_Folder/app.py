# # import the complete PyMongo library and check its version
# import pymongo
# print ("pymongo version:", pymongo.version)

# # import the MongoClient class
# from pymongo import MongoClient

# # build a new client instance for MongoDB passing
# # the string domain and integer port to the host parameters
# mongo_client = MongoClient('localhost', 27017)

# host_info = mongo_client['HOST']
# print ("\nhost:", host_info)


from flask import Flask, render_template, redirect, url_for
from flask.app import Flask
from flask_pymongo import PyMongo
import scraping

app = Flask(__name__)

## use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

## define the route for the HTML page
@app.route("/")
def index():
    mars = mongo.db.mars.find_one()
    return render_template("index.html", mars=mars)

@app.route("/scrape")
def scrape():
    mars = mongo.db.mars
    mars_data = scraping.scrape_all()
    mars.update_one({}, {"$set":mars_data}, upsert=True)
    return redirect('/', code=302)

if __name__ == "__main__":
    app.run()