from flask import Flask, request
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)
# Install VSCode-SQLite: https://stackoverflow.com/questions/40993895/how-to-see-a-sqlite-database-content-with-visual-studio-code.
# db.create_all()

# videos = {}

# def abort_if_video_id_doesnt_exist(video_id):
#     if video_id not in videos:
#         # 404 - Not Found.
#         abort(404, message="Could not find video...")

# def abort_if_video_exist(video_id):
#     if video_id not in videos:
#         # 409 - Conflict.
#         abort(409, message="Video already exists with that ID...")

class VideoModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    views = db.Column(db.Integer, nullable=False)
    likes = db.Column(db.Integer, nullable=False)

    # def __repr__(self):
    #     return f"Video(name = {name}, views = {views}, likes = {likes})"

video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str, help="Name of the video is required", required=True)
video_put_args.add_argument("views", type=int, help="Views of the video", required=True)
video_put_args.add_argument("likes", type=int, help="Likes on the video", required=True)

video_update_args = reqparse.RequestParser()
video_update_args.add_argument("name", type=str, help="Name of the video is required")
video_update_args.add_argument("views", type=int, help="Views of the video")
video_update_args.add_argument("likes", type=int, help="Likes on the video")

resource_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'views': fields.Integer,
    'likes': fields.Integer
}

class Video(Resource):
    # Return and serialize it with resource_fields format.
    @marshal_with(resource_fields)
    def get(self, video_id):
        # abort_if_video_id_doesnt_exist(video_id)
        # return videos[video_id]
        result = VideoModel.query.filter_by(id=video_id).first()
        if not result:
            # 404 - Not Found.
            abort(404, message="Could not find video with that id")
        return result
    
    @marshal_with(resource_fields)
    def put(self, video_id):
        # args = video_put_args.parse_args()
        # videos[video_id] = args
        # # https://developer.mozilla.org/en-US/docs/Web/HTTP/Status.
        # # 201 - Created.
        # return videos[video_id], 201
        args = video_put_args.parse_args()
        result = VideoModel.query.filter_by(id=video_id).first()
        if result:
            # 409 - Conflict.
            abort(409, message="Video id taken...")

        video = VideoModel(id=video_id, name=args['name'], views=args['views'], likes=args['likes'])
        db.session.add(video)
        db.session.commit()
        return video, 201

    @marshal_with(resource_fields)
    def patch(self, video_id):
        args = video_update_args.parse_args()
        result = VideoModel.query.filter_by(id=video_id).first()
        if not result:
            # 404 - Not Found.
            abort(404, message="Video doesn't exist, canont update")
        
        if args['name']:
            result.name = args['name']
        if args['views']:
            result.views = args['views']
        if args['likes']:
            result.likes = args['likes']

        db.session.commit()
        return result

    def delete(self, video_id):
        # abort_if_video_exist(video_id)
        # del videos[video_id]
        # # 204 - No Content.
        # return '', 204
        pass

api.add_resource(Video, "/video/<int:video_id>")

if __name__ == "__main__":
    app.run(debug=True)