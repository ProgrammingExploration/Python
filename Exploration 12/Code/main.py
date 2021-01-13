from flask import Flask
from flask_restful import Api, Resource, fields, marshal_with, reqparse
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)

class UserModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f'User with id: {self.id}'

user_create_args = reqparse.RequestParser()
user_create_args.add_argument('id', type=int, required=False)
user_create_args.add_argument('name', type=str, required=False)

resource_fields = {
    'id': fields.Integer,
    'name': fields.String
}

class Home(Resource):
    # @marshal_with(resource_fields)
    # def get(self, id):
    #     data = UserModel.query.get(id)
    #     print(data)
    #     if data == None:
    #         data = UserModel.query.all()
    #         return data
    #         # return f'User with {id} does not exist' (Does not work with Marshall With)
    #     else:
    #         return data

    @marshal_with(resource_fields)
    def get(self, id):
        try:
            data = UserModel.query.get(id)
            return data
        except:
            data = UserModel.query.all()
            return data

    @marshal_with(resource_fields)
    def post(self, id):
        args = user_create_args.parse_args()
        user = UserModel(name=args['name'])
        db.session.add(user)
        db.session.commit()
        return user
    
api.add_resource(Home, '/<int:id>')

if __name__ == '__main__':
    app.run(port=5000)
