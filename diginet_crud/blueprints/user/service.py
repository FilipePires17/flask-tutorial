from . import repository

def list_users():
    return [u.to_dict() for u in repository.get_all_users()]

def get_user(user_id):
    user = repository.get_user_by_id(user_id)
    return user.to_dict() if user else None

def create_user(data):
    return repository.create_user(data["name"], data["email"]).to_dict()

def update_user(user_id, data):
    user = repository.get_user_by_id(user_id)
    if not user:
        return None
    return repository.update_user(user, data["name"], data["email"]).to_dict()

def delete_user(user_id):
    user = repository.get_user_by_id(user_id)
    if not user:
        return False
    repository.delete_user(user)
    return True
