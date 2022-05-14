from ast import Pass
from flask import Flask, redirect, request, render_template, url_for, redirect
from flask_login import UserMixin
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, FloatField
from wtforms.validators import InputRequired, Length, ValidationError
from flask_bcrypt import Bcrypt
from datetime import datetime

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = 'thisisasecretkey'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# # videos = {}

# # def abort_if_video_id_doesnt_exist(video_id):
# #     if video_id not in videos:
# #         # 404 - Not Found.
# #         abort(404, message="Could not find video...")

# # def abort_if_video_exist(video_id):
# #     if video_id not in videos:
# #         # 409 - Conflict.
# #         abort(409, message="Video already exists with that ID...")

# # DATABASE TABLE
# class VideoModel(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(100), nullable=False)
#     views = db.Column(db.Integer, nullable=False)
#     likes = db.Column(db.Integer, nullable=False)

#     # def __repr__(self):
#     #     return f"Video(name = {name}, views = {views}, likes = {likes})"

# DATABASE TABLE ===============================================================
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(16), nullable=False, unique=True)
    password = db.Column(db.String(16), nullable=False)
    expenses = db.relationship('Expense', backref='user', lazy=True)

class Expense(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(16), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    updated_at = db.Column(db.String(32), nullable=False)
    username = db.Column(db.String(16), db.ForeignKey('user.id'), nullable=False)

# # FIELDS VALIDATION
# video_put_args = reqparse.RequestParser()
# video_put_args.add_argument("name", type=str, help="Name of the video is required", required=True)
# video_put_args.add_argument("views", type=int, help="Views of the video", required=True)
# video_put_args.add_argument("likes", type=int, help="Likes on the video", required=True)

# video_update_args = reqparse.RequestParser()
# video_update_args.add_argument("name", type=str, help="Name of the video is required")
# video_update_args.add_argument("views", type=int, help="Views of the video")
# video_update_args.add_argument("likes", type=int, help="Likes on the video")

# # SERIALIZE - Return in serialized json format, pair with @marshal_with decorator.
# resource_fields = {
#     'id': fields.Integer,
#     'name': fields.String,
#     'views': fields.Integer,
#     'likes': fields.Integer
# }

# class Video(Resource):
#     # Return and serialize it with resource_fields format.
#     @marshal_with(resource_fields)
#     def get(self, video_id):
#         # abort_if_video_id_doesnt_exist(video_id)
#         # return videos[video_id]
#         result = VideoModel.query.filter_by(id=video_id).first()
#         if not result:
#             # 404 - Not Found.
#             abort(404, message="Could not find video with that id")
#         return result
    
#     @marshal_with(resource_fields)
#     def put(self, video_id):
#         # args = video_put_args.parse_args()
#         # videos[video_id] = args
#         # # https://developer.mozilla.org/en-US/docs/Web/HTTP/Status.
#         # # 201 - Created.
#         # return videos[video_id], 201
#         args = video_put_args.parse_args()
#         result = VideoModel.query.filter_by(id=video_id).first()
#         if result:
#             # 409 - Conflict.
#             abort(409, message="Video id taken...")

#         video = VideoModel(id=video_id, name=args['name'], views=args['views'], likes=args['likes'])
#         db.session.add(video)
#         db.session.commit()
#         return video, 201

#     @marshal_with(resource_fields)
#     def patch(self, video_id):
#         args = video_update_args.parse_args()
#         result = VideoModel.query.filter_by(id=video_id).first()
#         if not result:
#             # 404 - Not Found.
#             abort(404, message="Video doesn't exist, canont update")
        
#         if args['name']:
#             result.name = args['name']
#         if args['views']:
#             result.views = args['views']
#         if args['likes']:
#             result.likes = args['likes']

#         db.session.commit()
#         return result

#     def delete(self, video_id):
#         # abort_if_video_exist(video_id)
#         # del videos[video_id]
#         # # 204 - No Content.
#         # return '', 204
#         pass

# api.add_resource(Video, "/video/<int:video_id>")

# FORM =========================================================================
class RegisterForm(FlaskForm):
    username = StringField(
        validators=[InputRequired(), Length(min=4, max=16)],
        render_kw={"placeholder": "Username"})
    password = PasswordField(
        validators=[InputRequired(), Length(min=4, max=16)],
        render_kw={"placeholder": "Password"})
    submit = SubmitField("Register")

    def validate_username(self, username):
        existing_user_username = User.query.filter_by(username=username.data).first()
        if existing_user_username:
            raise ValidationError("That username already exists. Please choose a different one.")

class LoginForm(FlaskForm):
    username = StringField(
        validators=[InputRequired(), Length(min=4, max=16)],
        render_kw={"placeholder": "Username"})
    password = PasswordField(
        validators=[InputRequired(), Length(min=4, max=16)],
        render_kw={"placeholder": "Password"})
    submit = SubmitField("Login")

class AddExpenseForm(FlaskForm):
    name = StringField(
        validators=[InputRequired(), Length(min=1, max=254)],
        render_kw={"placeholder": "Expense name"})
    amount = FloatField(
        validators=[InputRequired()],
        render_kw={"placeholder": "Amount"})
    submit = SubmitField("Add Expense")

class EditExpenseForm(FlaskForm):
    name = StringField(
        validators=[InputRequired(), Length(min=1, max=254)],
        render_kw={"placeholder": "Expense name"})
    amount = FloatField(
        validators=[InputRequired()],
        render_kw={"placeholder": "Amount"})
    submit = SubmitField("Save Expense")

# HELPER FUNCTION ==============================================================
def GetCurrentUsername():
    user_id = current_user.get_id()
    user = User.query.filter_by(id=user_id).first()
    return user.username

def GetDateTime():
    # Date time format: https://docs.python.org/2/library/time.html#time.strptime.
    now = datetime.now()
    return now.strftime("%d %B %Y, %I:%M %p")

# ROUTER =======================================================================
@app.route('/')
def home():
    data = [
        ("01-01-2020", 1597),
        ("02-01-2020", 1456),
        ("03-01-2020", 1908),
        ("04-01-2020", 896),
        ("05-01-2020", 755),
        ("06-01-2020", 433),
        ("07-01-2020", 1100),
        ("08-01-2020", 1235),
        ("09-01-2020", 1478),
    ]

    labels = [row[0] for row in data]
    values = [row[1] for row in data]

    return render_template('home.html', labels=labels, values=values)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data)
        new_user = User(username=form.username.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user)
                return redirect(url_for('dashboard'))
    # Pass the variable form to login.html.
    return render_template('login.html', form=form)

@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    username = GetCurrentUsername()
    expenses = Expense.query.filter_by(username=username)
    labels = [expense.name for expense in expenses]
    values = [expense.amount for expense in expenses]
    return render_template('dashboard.html', username=username, expenses=expenses, labels=labels, values=values, array_size=len(labels))

@app.route('/add_expense', methods=['GET', 'POST'])
def add_expense():
    form = AddExpenseForm()
    if form.validate_on_submit():
        # Insert into database.
        new_expense = Expense(name=form.name.data, amount=form.amount.data, updated_at=GetDateTime(), username=GetCurrentUsername())
        db.session.add(new_expense)
        db.session.commit()
        return redirect(url_for('dashboard'))
    return render_template('add_expense.html', form=form)

# flask_sqlalchemy CRUD operation: https://flask-sqlalchemy.palletsprojects.com/en/2.x/queries/.
@app.route('/edit_expense/<id>', methods=['GET', 'POST'])
def edit_expense(id):
    form = EditExpenseForm()
    expense = Expense.query.filter_by(id=id).first()
    if form.validate_on_submit():
        expense.name = form.name.data
        expense.amount = form.amount.data
        expense.updated_at = GetDateTime()
        db.session.commit()
        return redirect(url_for('dashboard'))
    return render_template('edit_expense.html', form=form, expense=expense)

@app.route('/delete_expense/<id>', methods=['GET', 'POST'])
def delete_expense(id):
    Expense.query.filter_by(id=id).delete()
    db.session.commit()
    return redirect(url_for('dashboard'))

if __name__ == "__main__":
    app.run(debug=True)