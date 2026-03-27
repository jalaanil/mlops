import pickle
from typing import Any
from fastapi import FastAPI
from pydantic import BaseModel
import os
from loguru import logger

from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    MODEL_PATH: str ="./model.bin"
    MODEL_VERSION: str = "not defined"

settings = Settings()


# with open("./models/2022-01.bin" , "rb") as f_in:
with open(settings.MODEL_PATH , "rb") as f_in:
    model = pickle.load(f_in)

logger.info(f"version is {settings.MODEL_VERSION}")

trip = {
    "PULocationID" : "43",
    "DOLocationID" : "238",
    "trip_distance": 1.26,
}

# prediction = model.predict(trip)
# print(prediction)

def prepare_features( raw_features: dict[str, Any]) -> dict[str,Any]:
    features = {}
    features["PULocationID"] = str( raw_features["PULocationID"])
    features["DOLocationID"] = str( raw_features["DOLocationID"])
    features["trip_distance"] = float( raw_features["trip_distance"])
    return features


def predict ( features: dict[str, Any]) -> float:
    preds = model.predict(features)
    return float(preds[0])


def postprocess(prediction: float) -> float:
    return prediction

#### server

class PredictRequest(BaseModel):
    PULocationID: str
    DOLocationID: str
    trip_distance: float

app = FastAPI()


@app.get("/")
def usenaother():
    return "Please use /predict"

@app.post("/predict")
def predict_endpoint( predict_request: PredictRequest) -> dict[str, Any]:
    prepared_features = prepare_features(  predict_request.model_dump())
    prediction = predict(prepared_features)
    final_prediction = postprocess(prediction)
    return dict(prediction=dict(duration=final_prediction))