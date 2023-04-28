from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class CRUDMixin():

  def save(self):
    db.session.add(self)
    db.session.commit()
    return self
  
  def delete(self):
    db.session.delete(self)
    db.session.commit()
    return