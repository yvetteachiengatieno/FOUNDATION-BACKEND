from flask import Blueprint, render_template

blueprint = Blueprint('simple_pages', __name__)


@blueprint.route('/')
def index():
  return render_template('simple_pages/index.html')

@blueprint.route('/blogs')
def features():
  return render_template('simple_pages/blogs.html')

@blueprint.route('/merch')
def merch():
  return render_template('simple_pages/merch.html')

@blueprint.route('/about')
def about():
  return render_template('simple_pages/about.html')