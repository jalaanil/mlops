import requests

url = "http://localhost:8000/predict"
trip = {
    "PULocationID" : "43",
    "DOLocationID" : "38",
    "trip_distance": 1.36,
}

response = requests.post( url, json=trip).json()
print(response)
#uv run python predict-test.py