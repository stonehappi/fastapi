from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends

from core.database import get_db
from modules.user.entity import User
from modules.user.model import UserModel

router = APIRouter(
    prefix='/user',
    tags=['user']
)


@router.get('')
def gets(db: Session = Depends(get_db)):
    return db.query(User).all()


@router.get('/{item_id}')
def get(item_id: int):
    return f'get by id = {item_id}'


@router.post('')
def create(item: UserModel):
    return f'create new user {item}'


@router.put('/{item_id}')
def update(item_id: int, item: UserModel):
    return f'update user id = {item_id} and value = {item}'


@router.delete('/{item_id}')
def update(item_id: int):
    return f'delete user id = {item_id}'
