from flask import Flask
from flask_restful import Api, Resource, fields, marshal_with, reqparse
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
api = Api(app)

db = SQLAlchemy(app)

class VideoModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    likes = db.Column(db.Integer, nullable=False)
    title = db.Column(db.String(400), nullable=False)
    views = db.Column(db.Integer, nullable=False)
    url = db.Column(db.String(1000), nullable=False)

    def __repr__(self):
        return f'{self.id} has {self.views} views and {self.likes} likes'

video_get_args = reqparse.RequestParser()
video_get_args.add_argument('id', required=False, type=int)
video_get_args.add_argument('title', required=False, type=str)

video_patch_args = reqparse.RequestParser()
video_patch_args.add_argument('title', required=False, type=str)
video_patch_args.add_argument('views', required=False, type=int)
video_patch_args.add_argument('likes', required=False, type=int)
video_patch_args.add_argument('id', required=True, type=int)

video_create_args = reqparse.RequestParser()
video_create_args.add_argument('title', required=True, type=str)
video_create_args.add_argument('url', required=True, type=str)

video_model = {
    'id': fields.Integer,
    'title': fields.String,
    'likes': fields.Integer,
    'views': fields.Integer,
    'url': fields.String
}

@app.route('/', methods=['GET'])
def home():
    return "Fetch to /api"

class App(Resource):
    @marshal_with(video_model)
    def get(self):
        args = video_get_args.parse_args()
        if args['title']:
            title_videos = VideoModel.query.filter_by(title=args['title']).all()
            return title_videos
        elif args['id']:
            video = VideoModel.query.get(args['id'])
            return video
        else:
            all = VideoModel.query.all()
            return all
    
    @marshal_with(video_model)
    def post(self):
        args = video_create_args.parse_args()
        video = VideoModel(title=args['title'], url=args['url'], likes=0, views=0)
        db.session.add(video)
        db.session.commit()
        return video
    
    def patch(self):
        args = video_patch_args.parse_args()
        if not args['id']:
            return False
        else:
            if args['title']:
                updated = VideoModel.query.filter_by(id=args['id']).update(dict(title=args['title']))
                db.session.commit()
                return True
            elif args['views']:
                updated = VideoModel.query.filter_by(id=args['id']).update(dict(views=args['views']))
                db.session.commit()
                return True
            elif args['likes']:
                updated = VideoModel.query.filter_by(id=args['id']).update(dict(likes=args['likes']))
                db.session.commit()
                return True
            else:
                return False

api.add_resource(App, '/api')

if __name__ == '__main__':
    app.run(port=5000)
else:
    print('Running from Imported File')
