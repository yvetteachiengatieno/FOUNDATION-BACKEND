from app.extensions.database import db, CRUDMixin


class Merchandise(db.Model, CRUDMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))
    price = db.Column(db.Numeric(10, 2))
