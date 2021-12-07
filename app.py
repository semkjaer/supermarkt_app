from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb+srv://sem:deka@cluster0.olmaj.mongodb.net/product_data?retryWrites=true&w=majority"
mongo = PyMongo(app)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/aanbiedingen', methods=['GET'])
def aanbiedingen():
    data = mongo.db.products.find({ 'aanbieding': { '$exists': True, '$nin': [[], [''], False] } })

    return render_template('aanbiedingen.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)