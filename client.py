import json
import requests

data = [[1, 2, 3, 4], [4, 3, 2, 1], [3, 2, 4, 1]]
url = "http://0.0.0.0:8000/predict/"

predictions = []
for record in data:
    payload = {"features": record}
    payload = json.dumps(payload)
    print(payload)
    response = requests.post(url=url, data=payload)
    predictions.append(response.json()["predicted_class"])
print(predictions)
