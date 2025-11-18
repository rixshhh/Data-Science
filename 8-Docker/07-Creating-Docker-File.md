# **📘 Notes: Creating a Docker Image (Flask App Example)**

## **1. Project Structure**

```
project/
│── app.py
│── Dockerfile
```

---

## **2. Flask App (app.py)**

(Your uploaded file)

```python
from flask import Flask
import os

app = Flask(__name__)

@app.route('/',methods=['GET'])
def home():
    return 'Hello World'

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port='5000')
```

This app runs on **port 5000** inside the container.

---

## **3. Dockerfile**

Typical Dockerfile for Flask:

```dockerfile
FROM python:3.8-alpine

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

CMD python app.py
```

---

## **4. Build Docker Image**

Use the following command:

```sh
docker build -t welcome-app .
```

Explanation:

* `docker build` → builds the image
* `-t welcome-app` → names/tag the image
* `.` → build using current directory

---

## **5. Run Docker Image as Container**

```sh
docker run -p 5000:5000 welcome-app
```

Explanation:

* `-p 5000:5000` → maps:

  * **host machine port 5000** → **container port 5000**
* `welcome-app` → image name

---

## **6. Output Explanation**

When you run the container, you see:

```
* Serving Flask app 'app'
* Debug mode: on
WARNING: This is a development server.
* Running on all addresses (0.0.0.0)
* Running on http://127.0.0.1:5000
* Running on http://172.17.0.2:5000
* Restarting with stat
* Debugger is active!
```

### Meaning:

* **0.0.0.0** → visible to all networks inside container
* **127.0.0.1:5000** → container’s local loopback
* **172.17.0.2:5000** → internal Docker network IP
* Mapped to your system at:
  👉 [http://localhost:5000](http://localhost:5000)

---

## **7. Access the Flask App**

Open your browser:

```
http://localhost:5000
```

Expected output:

```
Hello World
```

---

## **8. Useful Docker Commands**

### List images

```sh
docker images
```

### List containers

```sh
docker ps -a
```

### Stop container

```sh
docker stop <container_id>
```

### Remove container

```sh
docker rm <container_id>
```

---

## **Summary (Quick Revision Notes)**

* Write Flask app → `app.py`
* Create Dockerfile
* Build image → `docker build -t welcome-app .`
* Run container → `docker run -p 5000:5000 welcome-app`
* Open app → `http://localhost:5000`
* View logs/output inside terminal
