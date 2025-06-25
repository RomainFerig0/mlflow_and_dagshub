from fastapi import FastAPI
import pickle

app = FastAPI()
model = pickle.load(open("models/random_forest_model", "rb"))

@app.get("/predict")
def predict(x: float):
    y = model.predict([[x]])
    return {"input": x, "prediction": float(y[0])}
