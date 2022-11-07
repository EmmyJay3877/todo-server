from fastapi import FastAPI, APIRouter, Depends, HTTPException, status, Response
from .. import models, schemas
from typing import List
from sqlalchemy.orm import Session
from ..database import get_db


router = APIRouter(
    prefix="/todos"
)

@router.get("/")
def get_todos(db: Session=Depends(get_db)):
    todos = db.query(models.Todo).all()
    return todos

@router.get("/{id}")
def get_todo(id: int, db: Session=Depends(get_db)):
    todo = db.query(models.Todo).filter(models.Todo.id==id).first()
    if not todo:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, 
        detail= f"todo with id:{id} not found")
    return todo

@router.post("/", status_code=status.HTTP_201_CREATED)
def create_todo(todo: schemas.Todo, db: Session=Depends(get_db)):
    new_todo = models.Todo(**todo.dict())
    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)
    return new_todo

@router.put("/{id}")
def update_todo(id: int, updated_todo: schemas.Todo, db: Session=Depends(get_db)):
    todo_query = db.query(models.Todo).filter(models.Todo.id==id)
    todo = todo_query.first()
    if todo == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
        detail=f"todo with id {id} does not exist")
    todo_query.update(updated_todo.dict(), synchronize_session=False)
    db.commit()
    return todo_query.first()

@router.delete("/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_todo(id: int, db: Session=Depends(get_db)):
    todo_query = db.query(models.Todo).filter(models.Todo.id==id)
    todo = todo_query.first()
    if todo == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
        detail=f"todo with id {id} does not exist")
    todo_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)