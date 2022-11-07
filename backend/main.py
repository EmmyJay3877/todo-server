from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import todo
from . import models
from .database import engine


app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(todo.router)

@app.get("/")
def read_root():
    return {"Hello": "World"}