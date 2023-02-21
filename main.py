from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from core.database import engine, Base

from modules.user.controller import router as user_router
# from modules.teacher.controller import router as teacher_router

Base.metadata.create_all(bind=engine)
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(user_router)
# app.include_router(teacher_router)


@app.get('/')
async def welcome():
    return "Welcome to ASCSE"
