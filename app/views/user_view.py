# app/views/user_view.py

from fastapi import APIRouter, HTTPException
from app.controllers.user_controller import fetch_users, fetch_user, fetch_add_user, fetch_delete_user, fetch_update_user
from app.models.user_model import User

router = APIRouter()

@router.get("/users")
def get_users():
    return fetch_users()

@router.get("/users/{user_id}")
def get_user(user_id: int):
    user = fetch_user(user_id)
    if user:
        return user
    raise HTTPException(status_code=404, detail="Usuário não encontrado")

@router.post("/users/add")
def post_user(user: User):
    user = fetch_add_user(user.id, user.name, user.email)
    if user:
        return user
    raise HTTPException(status_code=400, detail="Erro ao criar usuário")

@router.delete("/users/delete/{user_id}")
def exclude_user(user_id: int):
    if fetch_delete_user(user_id):
        return {"message": "Usuário excluído com sucesso"}
    raise HTTPException(status_code=404, detail="Usuário não encontrado")


@router.patch("/users/update/{user_id}")
def update_user(user_id: int, user: User):
    if fetch_update_user(user_id, user.name, user.email):
        return {"message": "Usuário atualizado com sucesso"}
    raise HTTPException(status_code=404, detail="Usuário não encontrado")