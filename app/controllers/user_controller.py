# app/controllers/user_controller.py

from app.models.user_model import get_all_users, get_user_by_id, create_user, delete_user, update_user

def fetch_users():
    return get_all_users()

def fetch_user(user_id: int):
    return get_user_by_id(user_id)

def fetch_add_user(user_id: int, name: str, email: str):
    return create_user(user_id, name, email)

def fetch_delete_user(user_id: int):
    return delete_user(user_id)

def fetch_update_user(user_id: int, name: str, email: str):
    return update_user(user_id, name, email)

