#Flask server to serve up index.html files in the templates folder

from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

@app.route("/")
def index():
    mars = mongo.db.mars.find_one()
    return render_template("index.html", mars=mars)

# #confirm that /scrape is correct
@app.route("/scrape")
def scrape():
    #create mars collection in MongoDB mars database
    mars = mongo.db.mars

    #create mars collection in MongoDB mars Database
    marsdata = scrape_mars.scrape()
    mars.update({}, marsdata, upsert=True)

    return redirect("/",code=302)


if __name__ == "__main__":
    app.run(debug=True)

    


    



