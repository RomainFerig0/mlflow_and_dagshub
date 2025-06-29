from fastapi import FastAPI
import pickle

app = FastAPI()
model = pickle.load(open("models/random_forest_model/random_forest_model_2/model.pkl", "rb"))

from fastapi import Query

@app.get("/predict")
def predict(x: float = Query(0.0, title="Input value")):
    y = model.predict([[x]])
    return {"input": x, "prediction": float(y[0])}
