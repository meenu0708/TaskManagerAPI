from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from .. repository import todo
from .. import schemas, oauth2
from .. database import get_db


router=APIRouter(prefix="/todos",
    tags=['Task'])

@router.get('/')
def get_all(db:Session= Depends(get_db),current_user: schemas.User=Depends(oauth2.get_current_user)):
    return todo.task_all(db)

@router.post('/',status_code=status.HTTP_201_CREATED)
def create_task(request: schemas.TodoBase,db:Session= Depends(get_db),current_user: schemas.User=Depends(oauth2.get_current_user)):
    return todo.create_task(request,db)

@router.get('/{id}',status_code=200)
def show_task(id: int,db:Session= Depends(get_db),current_user: schemas.User=Depends(oauth2.get_current_user)):
   return todo.show_task(id,db)

@router.delete('/{id}',status_code=status.HTTP_204_NO_CONTENT)
def del_task(id: int,db:Session= Depends(get_db),current_user: schemas.User=Depends(oauth2.get_current_user)):
    return todo.del_task(id,db)

@router.put('/{id}',status_code=status.HTTP_202_ACCEPTED)
def update(id: int,request: schemas.TodoBase,db:Session= Depends(get_db),current_user: schemas.User=Depends(oauth2.get_current_user)):
    return todo.update(id,request,db)