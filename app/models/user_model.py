# app/models/user_model.py
from pydantic import BaseModel

fake_users_db = [
    {"id": 1, "name": "Alice", "email": "alice@example.com"},
    {"id": 2, "name": "Bob", "email": "bob@example.com"},
    {"id": 3, "name": "Charlie", "email": "charlie@example.com"},
]

class User(BaseModel):
    id: int
    name: str
    email: str

def get_all_users():
    return fake_users_db

def get_user_by_id(user_id: int):
    return next((user for user in fake_users_db if user["id"] == user_id), None)

def create_user(user_id: int, name: str, email: str):
    new_user = {
        "id": user_id,
        "name": name,
        "email": email
    }
    fake_users_db.append(new_user)
    return new_user

def delete_user(user_id: int):
    for user in fake_users_db:
        if user["id"] == user_id:
            fake_users_db.remove(user)
            return True
    return False

def update_user(user_id: int, name: str, email: str):
    for user in fake_users_db:
        if user["id"] == user_id:
            user["name"] = name
            user["email"] = email
            return user
    return None