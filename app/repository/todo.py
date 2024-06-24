from sqlalchemy.orm import Session
from .. import models, schemas
from fastapi import HTTPException, status

def task_all(db:Session):
    items=db.query(models.TodoItem).all()
    return items

def create_task(request: schemas.TodoBase,db:Session):
    new_task = models.TodoItem(title=request.title,
                           description=request.description,
                           completed=request. completed,
                           priority=request.priority,
                           due_date=request.due_date)
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task

def show_task(id: int,db:Session):
    task = db.query(models.TodoItem).filter(models.TodoItem.id == id).first()
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'Task with id {id} not found')
    return task

def del_task(id: int,db:Session):
    task=db.query(models.TodoItem).filter(models.TodoItem.id==id)
    if not task.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Task with id {id} not found")
    task.delete(synchronize_session=False)
    db.commit()
    return {"detail" : "deleted"}

def update(id: int,request: schemas.TodoBase,db:Session):
    task = db.query(models.TodoItem).filter(models.TodoItem.id == id)
    if not task.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Task with id {id} not found")
    task.update(request.dict())
    db.commit()
    return {'detail': 'updated'}