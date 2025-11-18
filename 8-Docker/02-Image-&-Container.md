

# **What is a Docker Image?**

A **Docker Image** is a **blueprint** or **template** used to create containers.

Think of it like:

* A *recipe* for making a dish
* A *class* in object-oriented programming
* A *snapshot* containing everything your app needs

### A Docker Image contains:

* Source code
* Libraries
* Dependencies
* Runtime (Node.js, Python, etc.)
* Configuration files
* OS-level files (minimal Linux layer)

💡 **Image = Read-only template**
You cannot edit it while running.

---

# **What is a Docker Container?**

A **Docker Container** is the **running instance** of a Docker image.

Think of it like:

* The *actual dish* cooked from the recipe
* An *object* created from a class
* A *running application* with its own environment

### A Docker Container:

* Is created from an image
* Runs your app in isolation
* Has its own filesystem
* Can start/stop/restart
* Is lightweight (shares OS kernel)

💡 **Container = Running environment created from an image**

---

## **Difference Between Docker Image and Docker Container**

| Feature    | Docker Image       | Docker Container                   |
| ---------- | ------------------ | ---------------------------------- |
| Nature     | Read-only          | Read-write                         |
| Purpose    | Blueprint/template | Running instance                   |
| Mutability | Cannot change      | Can change (data, logs, etc.)      |
| State      | Static             | Dynamic (start/stop/restart)       |
| Usage      | Build once         | Run many containers from one image |

---

## Real-Life Example

### Example: Running a Node.js Application

### **Docker Image**

Contains:

* Node.js runtime
* App.js
* package.json
* All dependencies
* Linux base layer

This is like **zip file containing everything needed to run the app**.

### **Docker Container**

When you run the image:

```
docker run node-app
```

A container starts and:

* Runs the Node.js app
* Listens on ports
* Generates logs
* Stores temporary data

This is the **actual running application**.

---

### Analogy (Very Easy)

| Concept          | Analogy                      |
| ---------------- | ---------------------------- |
| Docker Image     | A movie DVD                  |
| Docker Container | Playing the movie on your TV |

Or

| Concept          | Analogy                                   |
| ---------------- | ----------------------------------------- |
| Docker Image     | A blueprint of a house                    |
| Docker Container | The actual house built from the blueprint |

---

### Simple Commands

#### Create an image:

```
docker build -t myapp .
```

#### Run a container:

```
docker run myapp
```

#### List images:

```
docker images
```

#### List containers:

```
docker ps
```

---

### Summary (Easy to Remember)

* **Image = Template**
* **Container = Running instance of the template**
* You can create unlimited containers from one image
* Images are static, containers are active

