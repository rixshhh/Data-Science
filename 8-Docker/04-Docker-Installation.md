# **Docker Installation Steps**

### **1. Install Docker on Windows (Windows 10/11 – 64-bit, Pro/Home)**

#### **Step 1: Download Docker Desktop**

* Go to Docker official site:
  **[https://www.docker.com/products/docker-desktop](https://www.docker.com/products/docker-desktop)**

#### **Step 2: Run the Installer**

* Double-click the downloaded **Docker Desktop Installer.exe**
* Enable:

  * **WSL 2**
  * **Hyper-V** (if required)
* Installer will auto-enable virtualization features.

#### **Step 3: Sign In**

* Open Docker Desktop → Sign in with Docker Hub (optional but recommended)

#### **Step 4: Verify Installation**

Open PowerShell or CMD:

```sh
docker --version
docker run hello-world
```

If you see “Hello from Docker!”, installation is successful 🎉

---

# **2. Install Docker on macOS (Intel & M1/M2/M3 Apple Silicon)**

#### **Step 1: Download Docker Desktop**

* [https://www.docker.com/products/docker-desktop](https://www.docker.com/products/docker-desktop)

#### **Step 2: Install**

* Double-click `.dmg` file → Drag Docker into **Applications**

#### **Step 3: Open Docker**

* Start Docker Desktop
* Allow permissions if prompted

#### **Step 4: Verify**

```sh
docker --version
docker run hello-world
```

---

# **3. Install Docker on Ubuntu (BEST for Devs)**

#### **Step 1: Update system**

```sh
sudo apt update
sudo apt upgrade -y
```

#### **Step 2: Install dependencies**

```sh
sudo apt install apt-transport-https ca-certificates curl software-properties-common -y
```

#### **Step 3: Add Docker’s GPG Key**

```sh
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
```

#### **Step 4: Add Docker Repository**

```sh
sudo add-apt-repository \
"deb [arch=amd64] https://download.docker.com/linux/ubuntu \
$(lsb_release -cs) stable"
```

#### **Step 5: Install Docker Engine**

```sh
sudo apt update
sudo apt install docker-ce docker-ce-cli containerd.io -y
```

#### **Step 6: Start & enable Docker**

```sh
sudo systemctl start docker
sudo systemctl enable docker
```

#### **Step 7: Verify**

```sh
sudo docker run hello-world
```

#### **(Optional) Run Docker without sudo**

```sh
sudo usermod -aG docker $USER
newgrp docker
```
