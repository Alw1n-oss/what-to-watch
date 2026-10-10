from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite3"

app.config["SECRET_KEY"] = "RULES"

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Импорт модулей пакета должен быть в конце файла,
# чтобы избежать циклических импортов: эти модули
# сами импортируют app и db из opinions_app.
from opinions_app import views, error_handlers, cli_commands  # noqa: E402,F401
