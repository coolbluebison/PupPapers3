# Standard library imports
import os
# Remote library imports
from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
import secrets
from dotenv import load_dotenv
load_dotenv()

# Local imports


# deployed version uncomment below code, local version comment out below code
app = Flask(
    __name__,
    static_url_path='',
    static_folder='../client/dist',
    template_folder='../client/dist'
)

# Instantiate app, set attributes

# deployed version comment out below code, local version comment in below code
# app = Flask(__name__)

# Instantiate app, set attributes
# app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://puppapers_db_user:OVezbxSUAe2ypoo2MtK8u2qrx0o9CJ0k@dpg-clqf922e9h4c73am0n6g-a.oregon-postgres.render.com/puppapers_db"
# os.environ.get('DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False
app.secret_key = secrets.token_hex(16)


# Define metadata, instantiate db
metadata = MetaData(naming_convention={
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
})

db = SQLAlchemy(metadata=metadata)
migrate = Migrate(app, db)
db.init_app(app)

# Instantiate REST API
api = Api(app)

# Instantiate CORS
# CORS(app)

CORS(app, resources={r"/*": {"origins": "*"}})

# bcrypt = Bcrypt(app)