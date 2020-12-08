from flask import Flask, jsonify, render_template

app = Flask(__name__)

names = []

@app.route('/html')
def html():
    return render_template('index.html') # Looks in templates folder already

@app.route('/')
def home():
    return jsonify({
        "name": "OM"
    })

@app.route('/name/<string:name>')
def name_page(name):
    names.push(name)
    return jsonify({
        "name": name
    })

app.run(port=5000)
