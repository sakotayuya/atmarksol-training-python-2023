from flask import Flask, flash, redirect, url_for
from flask_login import LoginManager
from config import Config
from models.users import db, Users
from routes.error import error_blueprint
from routes.login import login_blueprint
from routes.user import user_blueprint

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))


@login_manager.unauthorized_handler
def unauthorized_handler():
    flash("ログインが必要なページです。<br>ログインしてください。", "error")
    return redirect(url_for("login.login"))


app.register_blueprint(error_blueprint)
app.register_blueprint(login_blueprint)
app.register_blueprint(user_blueprint)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
