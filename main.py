from fastapi import FastAPI
from pydantic import BaseModel
import joblib

app = FastAPI()
model = None
vectorizer = None

@app.on_event("startup")
def load_model():
    global model
    global vectorizer
    model = joblib.load("movie_review.pkl")
    vectorizer = joblib.load("vectorizer.pkl")

class moviereview(BaseModel):
    review:str

@app.get("/")
def home():
    return {"message": "Server Running"}

@app.post("/analysis")
def analysis(data:moviereview):
    review = data.review
    X = vectorizer.transform([review])
    analysis = model.predict(X)[0]
    if analysis ==1:
        sentiment = "Positive"
    else:
        sentiment = "Negative"
    return{
        "review":review,
        "analysis":str(sentiment)
    }

