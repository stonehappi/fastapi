# from sqlalchemy.orm import Session
# from fastapi import APIRouter
# from modules.teacher.model import TeacherModel
#
# router = APIRouter(
#     prefix='/teacher',
#     tags=['teacher']
# )
#
#
# @router.get('')
# def gets(db: Session = Depends(get_db)):
#     items = db.query(models.User).all();
#     return items;
#
#
# @router.get('/{item_id}')
# def get(item_id: int, db: Session = Depends(get_db)):
#     return f'get by id = {item_id}'
#
#
# @router.post('')
# def create(item: TeacherModel, db: Session = Depends(get_db)):
#     return f'create new user {item}'
#
#
# @router.put('/{item_id}')
# def update(item_id: int, item: TeacherModel, db: Session = Depends(get_db)):
#     return f'update user id = {item_id} and value = {item}'
#
#
# @router.delete('/{item_id}')
# def update(item_id: int, db: Session = Depends(get_db)):
#     return f'delete user id = {item_id}'
