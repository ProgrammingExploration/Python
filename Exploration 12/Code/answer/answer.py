from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

stores = [
  {
    'name': 'Store1'
  }
]

@app.route('/')
def home():
  return render_template('index.html')

#get /store/<name> data: {name :}
@app.route('/store/<string:name>')
def get_store(name):
  for store in stores:
    if store['name'] == name:
          return jsonify(store)
  return jsonify(stores)

# Get All Stores
@app.route('/all')
def all():
  return jsonify(stores)

#post /store data: {name :}
@app.route('/store', methods=['POST'])
def create_store():
  data = request.get_json()
  new_store = {
    'name': data['name']
  }
  stores.append(new_store)
  return jsonify(stores)

app.run(port=5000)
