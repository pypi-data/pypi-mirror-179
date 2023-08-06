# The Unofficial Flask IP Info Extension
This library provides simple access to the client's IP in `flask`.
```python
from flask import Flask, request
from flask_ip_api import IPInfo

app = Flask(__name__)
IPInfo(app)

@app.route("/")
def index():
  return request.ip["ip"]

if __name__ == "__main__":
  app.run()
```
Uses the [https://ipapi.com/](https://ipapi.com/) and [https://ipinfo.io/](https://ipinfo.io/) `IP` APIs.