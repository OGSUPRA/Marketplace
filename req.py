import requests

app_info = requests.get("http://localhost:8000/health").json()
print("App Info:", app_info)