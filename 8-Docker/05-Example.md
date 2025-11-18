
## **1. `docker hub` (Search on Docker Hub)**

Docker Hub is a public registry where all Docker **images** are stored.

When you search **"getting started"**, you find the official image:

```
docker/getting-started
```

---

## **2. Pulling the Image**

### Command:

```
docker pull docker/getting-started
```

### Meaning:

* **docker pull** = download an image from Docker Hub
* **docker/getting-started** = image name

After this, the image is stored locally.

---

## **3. Check if Image is Downloaded**

```
docker images
```

Shows:

* Image ID
* Size
* Version
* Repository name

---

## **4. Running the Image**

### Command:

```
docker run -d -p 80:80 docker/getting-started
```

Let’s break this:

### ✔ `docker run`

Creates and starts a new **container** from an image.

### ✔ `-d` (detached mode)

Runs the container **in background**, like a service.
Without `-d`, it runs in the terminal and blocks it.

### ✔ `-p 80:80` (port mapping)

Maps **host port** to **container port**.

Breakdown:

* **Left side (host port)** → `80`
* **Right side (container port)** → `80`

Meaning:

* Any request to **127.0.0.1:80** on your system
  will be forwarded inside the container at port **80**.

### ✔ `docker/getting-started`

The image used to create the container.

---

## **5. Difference Between Host Port vs Container Port**

### **Container Port**

* Port *inside* the container
* Where the application is running (for example, Node.js = 3000, Nginx = 80)

### **Host Port**

* Port *on your local machine*
* You use this port to access the container app

### Example (`80:80`)

| Host | Container |
| ---- | --------- |
| 80   | 80        |

So going to **127.0.0.1:80** in Chrome opens the container app.

### Example (`5000:80`)

| Host | Container |
| ---- | --------- |
| 5000 | 80        |

Now app is inside container at port **80**,
but you must visit:
👉 **localhost:5000**

---

## **6. Check Running Containers**

```
docker ps
```

You will see something like:

```
CONTAINER ID   IMAGE                    COMMAND                  CREATED         STATUS         PORTS                NAMES
12b3a67eb5b4   docker/getting-started   "/docker-entrypoint.…"   39 seconds ago  Up 35 seconds  0.0.0.0:80->80/tcp   sharp_bardeen
```

Meaning:

* Container is **up and running**
* Container port **80** is mapped to **host port 80**
* Random container name = `sharp_bardeen`

---

## **7. Access in Browser**

Open:

```
127.0.0.1:80
```

or simply:

```
localhost:80
```

You will see the "Getting Started" application.

---

## **8. Stop the Container**

Use either Container ID or container name:

```
docker stop 12b3a67eb5b4
```

or

```
docker stop sharp_bardeen
```

This stops the running container but does **not** delete it.

