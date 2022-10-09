from typing import Union

from fastapi import FastAPI

import shutil
import tempfile

from fastapi import APIRouter
from pyspark.context import SparkContext
from pyspark.sql.session import SparkSession
from starlette.responses import FileResponse
import pyspark.sql.functions as F

app = FastAPI()
# router = APIRouter()
sc = SparkContext('local')
spark = SparkSession(sc)

df = spark.read.option("header",True).csv("../data/all_data_csv")

@app.get("/")
def read_root():
    return {"Hello": "World"}


#clase chemical_list_json():

@app.post("/get_chemical_data/{chemical_name}")
def get_chemical_data(chemical_name: str):
    return df.filter(F.col('molecule_name') == f"{chemical_name}").toJSON().map(eval).collect()