import uvicorn, json, os
from fastapi import FastAPI
from db import password, username
# from pyspark.context import SparkContext
# from pyspark.sql.session import SparkSession

app = FastAPI()

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
SQLALCHEMY_DATABASE_URL = f"postgresql://{username}:{password}@postgres/postgres"


engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.post("/get_chemical_data/{chemical_name}")
async def get_chemical_data(chemical_name: str):
    return df.filter(F.col('molecule_name') == f"{chemical_name}").toJSON().map(eval).collect()


# if __name__ == "__main__":
#     uvicorn.run('main:app', host='0.0.0.0', port=8515)