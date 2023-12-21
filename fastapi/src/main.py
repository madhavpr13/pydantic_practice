from fastapi import FastAPI, HTTPException
from databases.database import engine
from databases import database_models as models

app = FastAPI()

models.Base.metadata.create_all(bind=engine)
