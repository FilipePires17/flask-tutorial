from .model import User
from extensions import db

def get_all_users():
    return User.query.all()

def get_user_by_id(user_id):
    return User.query.get(user_id)

def create_user(name, email):
    new_user = User(name=name, email=email)
    db.session.add(new_user)
    db.session.commit()
    return new_user

def update_user(user, name, email):
    user.name = name
    user.email = email
    db.session.commit()
    return user

def delete_user(user):
    db.session.delete(user)
    db.session.commit()
