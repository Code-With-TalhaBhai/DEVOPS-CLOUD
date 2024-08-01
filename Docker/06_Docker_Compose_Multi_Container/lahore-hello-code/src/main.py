from fastapi import FastAPI,Body
from sqlmodel import Field,Session,SQLModel,create_engine,select
from dotenv import load_dotenv
import os
from typing import List
from sqlalchemy import Column,Integer,String
from sqlalchemy.dialects.postgresql import ARRAY


class Students(SQLModel,table=True):
    # Used None with primary_key if we do not give value to id its value is by-default None before going to database, and then database auto-increment it
    id: int | None = Field(default=None,primary_key=True)
    name: str = Field(index=True) # For fast-retrieval of data costly operation
    age : int = Field(nullable=False)
    # here to start change to string
    # subjects: List[str] = Field(sa_column=Column(ARRAY(Integer))) # for integer array
    subjects: List[str] = Field(sa_column=Column(ARRAY(String))) # list of subjects

load_dotenv()
postgres_user = os.getenv('POSTGRES_USER')
postgres_password = os.getenv('POSTGRES_PASSWORD')
postgres_db = os.getenv('POSTGRES_DB')

connection_str = f'postgresql://{postgres_user}:{postgres_password}@postgres_container:5432/{postgres_db}' # inside container(`in connection string localhost replaced with container name`)
# connection_str = f'postgresql://{postgres_user}:{postgres_password}@localhost:81/{postgres_db}' # for local
engine = create_engine(connection_str,echo=True)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)




app = FastAPI()

@app.on_event("startup")
def on_startup():
    create_db_and_tables()


@app.get("/")
def root():
    return {"microservice": "This is a student management microservice "}


@app.get("/get-students")
async def get_students():
    students = []
    with Session(engine) as session:
        students = session.exec(select(Students)).all()
    return students
    

@app.post("/create-student")
# First way
# async def create_student(student_data:Students=Body(embed=True)):
#     print('student payload',type(student_data))
#     student_data = student_data.dict()
#     student = Students(name=student_data['name'],age=student_data['age'],subjects=student_data['subjects'])

# 2nd way
async def create_student(student_data:Students):
    with Session(engine) as session:
        session.add(student_data)
        session.commit()
        session.refresh(student_data)
        print('Added student id',student_data.id)
    return student_data


@app.get("/single-student/{id}")
async def single_student(id:int):
    student = {}
    with Session(engine) as session:
        stmt = select(Students).where(Students.id == id)
        student = session.exec(stmt).one()
    return student

        