from fastapi import FastAPI
import joblib
import numpy as np

model = joblib.load("app/model.joblib")
class_names = np.array(["setosa", "versicolor", "virginica"])
app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Iris model"}


@app.post("/predict/")
def predict(data: dict):
    feature = np.array(data["features"]).reshape(1, -1)
    prediction = model.predict(feature)
    print(prediction)
    class_name = class_names[prediction][0]
    return {"predicted_class": class_name}


print(predict({"features": [1, 2, 3, 4]}))
