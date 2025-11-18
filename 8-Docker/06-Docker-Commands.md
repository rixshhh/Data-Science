

# **Docker Commands Cheat Sheet**

---

## **1. Basic Docker Commands**

### ✔ Check Docker version

```sh
docker --version
docker version
```

### ✔ Check system-wide info

```sh
docker info
```

### ✔ Pull image from Docker Hub

```sh
docker pull <image_name>
```

Example:

```sh
docker pull ubuntu
```

### ✔ List all pulled images

```sh
docker images
```

### ✔ Remove an image

```sh
docker rmi <image_id_or_name>
```

---

## **2. Container Commands**

### ✔ Create & run a container

```sh
docker run <image_name>
```

### ✔ Run container with interactive terminal

```sh
docker run -it <image_name> bash
```

### ✔ Run in background (detached mode)

```sh
docker run -d <image_name>
```

### ✔ Run container with port mapping

```sh
docker run -p <host_port>:<container_port> <image_name>
```

Example:

```sh
docker run -p 8080:80 nginx
```

### ✔ Run container with a custom name

```sh
docker run --name mycontainer <image_name>
```

### ✔ List running containers

```sh
docker ps
```

### ✔ List all containers (including stopped)

```sh
docker ps -a
```

### ✔ Stop a running container

```sh
docker stop <container_id>
```

### ✔ Start a stopped container

```sh
docker start <container_id>
```

### ✔ Restart container

```sh
docker restart <container_id>
```

### ✔ Remove a container

```sh
docker rm <container_id>
```

### ✔ Remove all stopped containers

```sh
docker container prune
```

---

## **3. Inspect & Logs**

### ✔ View logs

```sh
docker logs <container_id>
```

### ✔ Follow logs like tail -f

```sh
docker logs -f <container_id>
```

### ✔ Inspect container details (JSON format)

```sh
docker inspect <container_id>
```

### ✔ Show resource usage

```sh
docker stats
```

---

## **4. Execute Commands Inside a Container**

### ✔ Run a command inside a running container

```sh
docker exec <container_id> <command>
```

Example:

```sh
docker exec myapp ls /
```

### ✔ Open bash shell inside container

```sh
docker exec -it <container_id> bash
```

---

## **5. Docker Image Build Commands**

### ✔ Build an image using Dockerfile

```sh
docker build -t <image_name> .
```

### ✔ Tag an image

```sh
docker tag <image> <new_tag>
```

### ✔ Remove unused images

```sh
docker image prune
```

### ✔ Remove all unused images

```sh
docker image prune -a
```

---

## **6. Docker Network Commands**

### ✔ List networks

```sh
docker network ls
```

### ✔ Create a network

```sh
docker network create <network_name>
```

### ✔ Inspect a network

```sh
docker network inspect <network_name>
```

### ✔ Connect container to network

```sh
docker network connect <network_name> <container_id>
```

---

## **7. Docker Volume Commands**

### ✔ List volumes

```sh
docker volume ls
```

### ✔ Create volume

```sh
docker volume create <volume_name>
```

### ✔ Inspect volume

```sh
docker volume inspect <volume_name>
```

### ✔ Remove volume

```sh
docker volume rm <volume_name>
```

---

## **8. Clean Up Commands**

### ✔ Remove all stopped containers, unused images, networks

```sh
docker system prune
```

### ✔ Clean everything (dangerous)

```sh
docker system prune -a
```

---

## **9. Docker Compose Commands**

### ✔ Start services

```sh
docker-compose up
```

### ✔ Start in background

```sh
docker-compose up -d
```

### ✔ Stop

```sh
docker-compose down
```

### ✔ Restart services

```sh
docker-compose restart
```

### ✔ View logs

```sh
docker-compose logs
```
