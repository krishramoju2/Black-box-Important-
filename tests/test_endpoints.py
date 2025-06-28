# tests/test_endpoints.py
import requests

def test_endpoint1():
    url = "http://localhost:8000/endpoint1"
    payload = {"input": "hello"}
    res = requests.post(url, json=payload)
    print("Response from endpoint1:", res.json())

if __name__ == "__main__":
    test_endpoint1()
