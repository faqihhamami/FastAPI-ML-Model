import requests

URL = "http://localhost:8000/predict"

ads = {
  "tv": 292.9,
  "radio": 0,
  "newspaper": 0
}

response = requests.post(URL, json=ads)
prediction = response.json()

print("Car price prediction: ", prediction)