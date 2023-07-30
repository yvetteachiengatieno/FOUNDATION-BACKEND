from flask import Blueprint, render_template, request,url_for,redirect
from app.users.models import User
from werkzeug.security import generate_password_hash, check_password_hash

blueprint = Blueprint('users', __name__)

@blueprint.get('/register')
def get_register():
  return render_template('users/register.html')

@blueprint.post('/register')
def post_register():
    try:
      if request.form.get('password') != request.form.get('password_confirmation'):
        raise Exception('The password confirmation must match the password.')
      elif User.query.filter_by(email=request.form.get('email')).first():
        raise Exception('The email address is already registered.')
      user = User(
        email= request.form.get('email'),
        password=generate_password_hash(request.form.get('password'))
      )
      user.save()

      return redirect (url_for('simple_pages.index'))
    except Exception as error_message:
        error = error_message or 'An error occurred while creating a user. Please make sure to enter valid data.'
        return render_template('users/register.html', error=error)
      

@blueprint.get('/login')
def get_login():
  return render_template('users/login.html')

@blueprint.post('/login')
def post_login():
  try:
    user = User.query.filter_by(email=request.form.get('email')).first()

    if not user:
      raise Exception('No user with the given email address was found.')
    elif not check_password_hash(user.password, request.form.get('password')):
      raise Exception('The password does not appear to be correct.')
    
    return redirect(url_for('merchandise.merchandise'))
    
  except Exception as error_message:
    error = error_message or 'An error occurred while logging in. Please verify your email and password.'
    return render_template('users/login.html', error=error)

@blueprint.get('/logout')
def logout():
  return 'User logged out'