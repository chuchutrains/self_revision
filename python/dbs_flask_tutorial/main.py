from flask import Flask, redirect, render_template, url_for, redirect, flash
from flask_login import UserMixin
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
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

# HELPER FUNCTION ==============================================================
def getCurrentUsername():
    user_id = current_user.get_id()
    user = User.query.filter_by(id=user_id).first()
    return user.username

def getDateTime():
    # Date time format: https://docs.python.org/2/library/time.html#time.strptime.
    now = datetime.now()
    # Eg. 21 May 2022, 12:50 AM.
    return now.strftime("%d %B %Y, %I:%M %p")

def isFloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

# FORM =========================================================================
U_PWD_MIN_LEN = 4
U_PWD_MAX_LEN = 16
NAME_MIN_LEN = 1
NAME_MAX_LEN = 254

class RegisterForm(FlaskForm):
    username = StringField(
        validators=[InputRequired(), Length(min=U_PWD_MIN_LEN, max=U_PWD_MAX_LEN)],
        render_kw={"placeholder": "Username"})
    password = PasswordField(
        validators=[InputRequired(), Length(min=U_PWD_MIN_LEN, max=U_PWD_MAX_LEN)],
        render_kw={"placeholder": "Password"})
    submit = SubmitField("Register")

    # Custom validation: https://wtforms.readthedocs.io/en/3.0.x/validators/#custom-validators.
    def validate_username(self, username):
        existing_user_username = User.query.filter_by(username=username.data).first()
        if existing_user_username:
            # Display error message at .html using Jinja syntax.
            raise ValidationError("Username already exists, please choose a different one.")

class LoginForm(FlaskForm):
    username = StringField(
        validators=[InputRequired(), Length(min=U_PWD_MIN_LEN, max=U_PWD_MAX_LEN)],
        render_kw={"placeholder": "Username"})
    password = PasswordField(
        validators=[InputRequired(), Length(min=U_PWD_MIN_LEN, max=U_PWD_MAX_LEN)],
        render_kw={"placeholder": "Password"})
    submit = SubmitField("Login")

class AddExpenseForm(FlaskForm):
    name = StringField(
        validators=[InputRequired(), Length(min=NAME_MIN_LEN, max=NAME_MAX_LEN)],
        render_kw={"placeholder": "Expense name"})
    amount = StringField(
        validators=[InputRequired()],
        render_kw={"placeholder": "Amount"})
    submit = SubmitField("Add Expense")

    def validate_amount(self, amount):
        amount_str = amount.data 
        if isFloat(amount_str) == False:
            raise ValidationError("Please use only numbers in the Amount field.")
        elif amount_str.find('.')+2 != len(amount_str)-1:
            raise ValidationError("Please use only 2 decimal point in the Amount field.")

class EditExpenseForm(FlaskForm):
    name = StringField(
        validators=[InputRequired(), Length(min=NAME_MIN_LEN, max=NAME_MAX_LEN)],
        render_kw={"placeholder": "Expense name"})
    amount = StringField(
        validators=[InputRequired()],
        render_kw={"placeholder": "Amount"})
    submit = SubmitField("Save Expense")

    def validate_amount(self, amount):
        amount_str = amount.data 
        if isFloat(amount_str) == False:
            raise ValidationError("Please use only numbers in the Amount field.")
        elif amount_str.find('.')+2 != len(amount_str)-1:
            raise ValidationError("Please use only 2 decimal point in the Amount field.")

# ROUTER =======================================================================
@app.route('/')
def home():
    return render_template('index.html')

# Url end point.
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data)
        new_user = User(username=form.username.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))
    # Pass the variable form to login.html.
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user)
                return redirect(url_for('dashboard'))
            else:
                flash("Your Username or Password is incorrect")
        else:
            flash("Sorry, you have entered an invalid Username")
    return render_template('login.html', form=form)

@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    username = getCurrentUsername()
    expenses = Expense.query.filter_by(username=username)
    labels = [expense.name for expense in expenses]
    values = [expense.amount for expense in expenses]
    return render_template('dashboard.html', expenses=expenses, labels=labels, values=values)

@app.route('/addExpense', methods=['GET', 'POST'])
def addExpense():
    form = AddExpenseForm()
    if form.validate_on_submit():
        # Insert into database.
        new_expense = Expense(name=form.name.data, amount=form.amount.data, updated_at=getDateTime(), username=getCurrentUsername())
        db.session.add(new_expense)
        db.session.commit()
        return redirect(url_for('dashboard'))
    return render_template('addExpense.html', form=form)

# flask_sqlalchemy CRUD operation: https://flask-sqlalchemy.palletsprojects.com/en/2.x/queries/.
@app.route('/editExpense/<id>', methods=['GET', 'POST'])
def editExpense(id):
    form = EditExpenseForm()
    expense = Expense.query.filter_by(id=id).first()
    if form.validate_on_submit():
        expense.name = form.name.data
        expense.amount = form.amount.data
        expense.updated_at = getDateTime()
        db.session.commit()
        return redirect(url_for('dashboard'))
    return render_template('editExpense.html', form=form, expense=expense)

@app.route('/deleteExpense/<id>', methods=['GET', 'POST'])
def deleteExpense(id):
    Expense.query.filter_by(id=id).delete()
    db.session.commit()
    return redirect(url_for('dashboard'))

if __name__ == "__main__":
    app.run(debug=True)