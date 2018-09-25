from flask import Flask, render_template, redirect
from scrape_mars import scrape
import pymongo

app = Flask(__name__)

client = pymongo.MongoClient('mongodb://localhost:27017')
db = client.mars_db
collection = db.mars_facts

@app.route('/')
def home():
	mars_facts = collection.find_one()
	return render_template('index.html', mars_facts=mars_facts)

#Create route that will trigger scrape functions
@app.route('/scrape')
def mars_scrape():
	scrape_info = scrape()
	# Insert scrape into database
	collection.drop()
	collection.insert_one(scrape_info)
	# Redirect back to home page
	return redirect('/', code=302)

if __name__ =='__main__':
	app.run(debug=True)	


