from flask import Flask, redirect, url_for, render_template
from . import merchandise, simple_pages
from app.extensions.database import db



app = Flask(__name__)
app.config.from_object('app.config')
app.register_blueprint(merchandise.routes.blueprint)
app.register_blueprint(simple_pages.routes.blueprint)
db.init_app(app)





