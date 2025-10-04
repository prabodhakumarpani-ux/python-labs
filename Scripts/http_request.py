import requests
url = "https://httpbin.org/get"
r = requests.get(url, timeout=10)
print("Status:", r.status_code)
print("Headers:", dict(r.headers))
print("Origin:", r.json().get("origin"))
