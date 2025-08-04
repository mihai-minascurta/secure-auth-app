from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)

app.config['SECRET_KEY'] = 'any-secret-key-you-choose'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

##Portalul de login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

##CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
#Line below only required once, when creating DB. 
# db.create_all()

@app.route('/')
def home():
    if current_user.is_authenticated:
        return redirect(url_for('secrets'))
    all_users = db.session.query(User).all()
    print(all_users)
    return render_template("index.html", logged_in=False)

@app.route('/register' , methods=["GET" , "POST"])
def register():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]

        existing_email = User.query.filter_by(email = email).first()
        if existing_email:
            flash("Email ul a fost deja folosit!")
            return redirect(url_for('register'))

        print(name , email , password)

        if name is not None and email is not None and password is not None:
            hashed_password = generate_password_hash(password = password , method= "pbkdf2:sha256" , salt_length = 8)
            new_user = User(name = name , email = email , password = hashed_password)
            db.session.add(new_user)
            db.session.commit()
            return render_template("secrets.html" , name=name)
        
    return render_template("register.html")

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/login' , methods=["GET" , "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        user = User.query.filter_by(email = email).first()

        if user and check_password_hash(pwhash = user.password , password = password):
            login_user(user)
            print(f"Utilizatorul cu email ul {user.email} s-a logat cu succes")
            return render_template("secrets.html" , name = user.name)
        elif user:
            flash("Parola gresita")
            return redirect(url_for("login"))
        else:
            flash("Email ul introdus este inexistent")
            return redirect(url_for('login'))
    return render_template("login.html")

@app.route('/secrets')
@login_required
def secrets():
    return render_template("secrets.html")

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return render_template("index.html")

@app.route('/download')
def download():
    return send_from_directory(
        directory='static/files',
        path='cheat_sheet.pdf',
        as_attachment=True  # => forțează descărcarea
    )
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
