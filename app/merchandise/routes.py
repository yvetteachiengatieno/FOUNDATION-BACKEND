from flask import Blueprint, render_template, request, redirect, url_for
from app.merchandise.models import Merchandise

blueprint = Blueprint('merchandise', __name__)

@blueprint.get("/edit_item/<id>")
def show_edit_item(id):
  item = Merchandise.query.filter_by(id=id).first()
  

  return render_template("merchandise/edit.html", item=item)

@blueprint.post("/edit_item")
def edit_item():
  target = request.form.get("id")
  item = Merchandise.query.filter_by(id=target).first()
  
  name = request.form.get("name")
  description = request.form.get ("description")
  price = request.form.get("price")

  item.name = name
  item.description = description
  item.price = price 

  item.save()

  return redirect(url_for("merchandise.index"))


@blueprint.post("/delete")
def delete_item():
  target = request.form.get("id")
  item = Merchandise.query.filter_by(id=target).first()
  item.delete()
  return redirect(url_for("merchandise.index"))

@blueprint.route('/merchandise')
def index():
  merchandise = Merchandise.query.all()
  return render_template('merchandise/index.html', merchandise=merchandise)

@blueprint.route('/merchandise/<id>')
def item(id):
  item = Merchandise.query.filter_by(id=id).first()
  return render_template('merchandise/show.html', item=item)

@blueprint.get('/merchandise/new')
def new_merchindise():
  return render_template('merchandise/new.html')

@blueprint.post('/merchandise/new')
def save_merchindise():
  page = "merchandise/new.html"
  validation = [
    request.form.get('name'),
    request.form.get('description'),
    request.form.get('price'),
  ]

  if not all(validation):
    return render_template(page, error='Please fill out all address fields.')
  
  merchandise = Merchandise(
    name=request.form.get('name'),
    description=request.form.get('description'),
    price=request.form.get('price')
  )
  merchandise.save()
  return render_template('merchandise/new.html', message="{} saved successfuly".format(merchandise.name))