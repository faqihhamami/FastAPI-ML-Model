
import uvicorn
import joblib
import pandas as pd
import numpy as np

from fastapi import FastAPI
from pydantic import BaseModel

class Sales(BaseModel):
    tv : float 
    radio : float 
    newspaper : float


app = FastAPI()

@app.get("/")
def read_root():
    return {"Predict": "total sales"}


@app.post("/predict")
def sales(sales: Sales):

    model_pkl_file = "model/model_lr.pkl"
    model_rf = joblib.load(model_pkl_file)

    # Create a series and select the features the current model expects
    input_data = np.array([sales.tv])
    
    prediction = model_rf.predict(input_data.reshape(-1,1))

    # Cast the prediction to int
    prediction = int(prediction[0])

    return prediction


## How to run
# open cmd and run : uvicorn main:app --reload
# open browser and type : http://127.0.0.1:8000
# or open http://127.0.0.1:8000/docs
