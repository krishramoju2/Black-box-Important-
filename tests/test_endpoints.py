import requests

def test_endpoint1():
    url = "http://localhost:8000/endpoint1"
    payload = {"input": "hello"}
    res = requests.post(url, json=payload)
    print("[endpoint1] Input: hello →", res.json())

def test_endpoint2_even_length():
    url = "http://localhost:8000/endpoint2"
    payload = {"input": "test"}  # even length → reverse
    res = requests.post(url, json=payload)
    print("[endpoint2] Input: test (even) →", res.json())

def test_endpoint2_odd_length():
    url = "http://localhost:8000/endpoint2"
    payload = {"input": "abc"}  # odd length → uppercase
    res = requests.post(url, json=payload)
    print("[endpoint2] Input: abc (odd) →", res.json())

if __name__ == "__main__":
    print("== Testing Endpoint 1 ==")
    test_endpoint1()
    print("\n== Testing Endpoint 2 (Even Length) ==")
    test_endpoint2_even_length()
    print("\n== Testing Endpoint 2 (Odd Length) ==")
    test_endpoint2_odd_length()
