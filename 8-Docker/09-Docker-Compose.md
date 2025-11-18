# **What is Docker Compose?**

**Docker Compose** is a tool that lets you run **multiple Docker containers** using a **single YAML file** (`docker-compose.yml`).

It is used when your project needs more than one service, like:

* Backend (Node.js / Python / Java)
* Frontend (React / Next.js)
* Database (MongoDB / MySQL / PostgreSQL)
* Caching (Redis)
* Message queue (RabbitMQ)

Instead of manually running many `docker run` commands, Compose lets you run everything with:

```
docker-compose up -d
```

---

# **What is `.env` in Docker Compose?**

The `.env` file stores environment variables.
This helps you avoid hardcoding secrets or config inside `docker-compose.yml`.

Example values in `.env`:

```
MONGO_USER=admin
MONGO_PASSWORD=12345
APP_PORT=8080
```

You can use these variables inside `docker-compose.yml` like:

```
${APP_PORT}
${MONGO_USER}
${MONGO_PASSWORD}
```

---

## **Example: Node.js App + MongoDB using Docker Compose**

### ✔ Project structure:

```
project/
 ├── docker-compose.yml
 ├── .env
 └── app/
      └── Dockerfile
```

---

### **1. .env File**

Create `.env` in root:

```env
APP_PORT=5000
MONGO_INITDB_ROOT_USERNAME=admin
MONGO_INITDB_ROOT_PASSWORD=secret123
MONGO_PORT=27017
```

---

### **2. docker-compose.yml**

```yaml
version: "3.9"

services:
  app:
    build: ./app
    ports:
      - "${APP_PORT}:5000"
    environment:
      - MONGO_URL=mongodb://admin:secret123@mongo:27017/
    depends_on:
      - mongo

  mongo:
    image: mongo:latest
    ports:
      - "${MONGO_PORT}:27017"
    environment:
      - MONGO_INITDB_ROOT_USERNAME=${MONGO_INITDB_ROOT_USERNAME}
      - MONGO_INITDB_ROOT_PASSWORD=${MONGO_INITDB_ROOT_PASSWORD}
    volumes:
      - mongo_data:/data/db

volumes:
  mongo_data:
```

---

### **3. Dockerfile (inside app folder)**

```dockerfile
FROM node:18

WORKDIR /app

COPY package.json .
RUN npm install

COPY . .

CMD ["npm", "start"]
```

---

### **Run everything**

Start services:

```
docker-compose up -d
```

Stop services:

```
docker-compose down
```

Check logs:

```
docker-compose logs -f
```

---

### **Why use Docker Compose?**

| Feature                   | Benefit                           |
| ------------------------- | --------------------------------- |
| Start multiple containers | One command                       |
| Environment variables     | Cleaner, more secure              |
| Networking                | Containers can talk to each other |
| Volumes                   | Persistent storage                |
| Easily reproducible       | Same setup on any machine         |

---