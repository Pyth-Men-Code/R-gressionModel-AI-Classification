import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url, json={'age':67, 'sex':'female','bmi':20.000,'children':1, 'smoker':'no','region':'southest'})

print(r.json())