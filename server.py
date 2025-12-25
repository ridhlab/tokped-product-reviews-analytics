from fastapi import FastAPI
from pydantic import BaseModel
import pickle
from utils.preprocess import preprocess_text

app = FastAPI()

# Load model once at startup
with open("models/model-package.pkl", "rb") as f:
    model_package = pickle.load(f)

MODEL = model_package["model"]
VECTORIZER = model_package["vectorizer"]


class PredictRequest(BaseModel):
    text: str


@app.get("/")
def root():
    return {
        "message": "Welcome to tokped product reviews sentiment analytics.\n"
        "This api to test message product reviews sentiment.\n"
        "This model used training data from https://www.kaggle.com/datasets/musabiam/tokopedia-product-and-review-dataset"
    }


@app.post("/predict")
def predict(request: PredictRequest):
    text = request.text
    processing_text = preprocess_text(text)
    text_vec = VECTORIZER.transform([processing_text])
    predict = MODEL.predict(text_vec)[0]
    return {"predict": predict}
