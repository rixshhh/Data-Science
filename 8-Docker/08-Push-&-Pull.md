

# **How to Push a Docker Image to Docker Hub**

---

## **Step 1 : Log in to Docker Hub**

You must log in before pushing.

### **Command**

```sh
docker login
```

### **Important Note (Windows PowerShell Issue)**

If password is **not visible** while typing — this is **normal**.
Docker does **not show password** for security. Just type your password and press **Enter**.

#### **If login fails**

Use a **Personal Access Token (PAT)** instead of Docker password.

🔗 Create Token:
[https://hub.docker.com/settings/security](https://hub.docker.com/settings/security)

Copy the token → paste it when asked for password.

---

## **Step 2 : Tag Your Local Docker Image**

Before pushing, your image **must be tagged** with your Docker Hub username.

### Syntax:

```sh
docker tag local-image-name username/repo-name:tag
```

---

## **Step 3 : Push the Image to Docker Hub**

### **Command**

```sh
docker push username/repo-name:tag
```

If login is successful, the image will start uploading.

---

## **Step 4: Verify on Docker Hub**

Go to:

```
https://hub.docker.com/repositories/username
```

You will see:

✔ Image name: `welcome-app`
✔ Tag: `latest`

---

## **Complete Example Workflow**

```sh
docker login
docker build -t welcome-app .
docker tag welcome-app username/repo-name:tag
docker push username/repo-name:tag
```

---

## Common Errors + Fixes

| Error                                                | Reason                             | Fix                                        |
| ---------------------------------------------------- | ---------------------------------- | ------------------------------------------ |
| `unauthorized: incorrect username/password`          | Password incorrect or SSO required | Use Personal Access Token (PAT)            |
| `denied: requested access to the resource is denied` | Image not tagged properly          | Use `docker tag` before push               |
| `repository does not exist`                          | Repo not created                   | Docker Hub auto-creates repo on first push |

---

## Summary

### To push image:

1. `docker login`
2. `docker tag local-image username/repo:tag`
3. `docker push username/repo:tag`

---

# **How to Run Your Docker Image on Any Machine**

Once you push the image to Docker Hub:

```
username/repo-name:tag
```

any machine can pull and run it.

---

## **Install Docker (only once per machine)**

Download Docker Desktop:

* Windows → [https://www.docker.com/products/docker-desktop](https://www.docker.com/products/docker-desktop)
* macOS → same link
* Linux → `sudo apt install docker.io`

---

## **Pull Your Image from Docker Hub**

On any machine, run:

```sh
docker pull username/repo-name:tag
```

Docker will download the image automatically.

---

## **Run the Container**

Example (for port 80 app):

```sh
docker run -d -p 80:80 username/repo-name:tag
```

### 📌 Explanation

| Command      | Meaning                                      |
| ------------ | -------------------------------------------- |
| `docker run` | Run a new container                          |
| `-d`         | Run in background (detached mode)            |
| `-p 80:80`   | Map **host port 80** → **container port 80** |
| `image-name` | Your Docker Hub image                        |

---

## **Verify Container Is Running**

```sh
docker ps
```

---

## **Access the Application (Any Machine)**

In browser:

```
http://localhost:80
```

Or, if in cloud VM:

```
http://<PUBLIC-IP>:80
```

Example:

```
http://13.232.10.95:80
```

---

## **Stop the Container**

```sh
docker stop <container-id>
```

---

## **Full Workflow on Another Machine**

```sh
docker pull username/repo-name:tag
docker run -d -p 80:80 username/repo-name:tag
docker ps
```

That’s it — your container will run exactly the same on **Windows, Linux, macOS, and Cloud servers**.

---

