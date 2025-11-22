# **GIT & GITHUB – IMPORTANT COMMANDS WITH DESCRIPTION**

---

## 🔹 **1. Git Installation & Setup**

### **Check Git version**

```
git --version
```

### **Set your username**

```
git config --global user.name "Your Name"
```

### **Set your email**

```
git config --global user.email "your@email.com"
```

### **Check your config**

```
git config --list
```

---

## 🔹 **2. Create a New Git Repository**

### **Initialize Git inside a project**

```
git init
```

### **Clone a GitHub repository**

```
git clone <repo-url>
```

Example:

```
git clone https://github.com/user/project.git
```

---

## 🔹 **3. Staging & Committing Files**

### **Check file status**

```
git status
```

### **Add a single file to staging**

```
git add filename
```

### **Add all files**

```
git add .
```

### **Commit the staged files**

```
git commit -m "Meaningful commit message"
```

### **Commit all changes (skip staging)**

```
git commit -a -m "Commit message"
```

---

## 🔹 **4. Branching Commands**

### **Create new branch**

```
git branch branchname
```

### **Switch to a branch**

```
git checkout branchname
```

### **Create & switch to branch**

```
git checkout -b new-branch
```

### **List all branches**

```
git branch
```

### **Delete a branch**

```
git branch -d branchname
```

---

## 🔹 **6. Merging Branches**

### **Merge a branch into current branch**

```
git merge branchname
```

Example: merge "feature" into "main":

```
git checkout main
git merge feature
```

---

## 🔹 **7. Undoing Changes**

### **Unstage added files**

```
git reset filename
```

### **Undo last commit but keep files**

```
git reset --soft HEAD~1
```

### **Undo last commit and remove file changes**

```
git reset --hard HEAD~1
```

### **Restore a file**

```
git checkout -- filename
```

---

## 🔹 **8. Git Log & History**

### **View commit history**

```
git log
```

### **Short log**

```
git log --oneline
```

### **See changes in commit**

```
git show <commit-id>
```

---

## 🔹 **9. GitHub Commands (Extra Useful)**

### **Create README**

```
echo "# Project Title" >> README.md
```

### **Check difference in files**

```
git diff
```

### **Remove a file**

```
git rm filename
```

### **Rename a file**

```
git mv oldname newname
```

---

## 🔹 **10. GitHub Authentication (HTTPS)**

When pushing for the first time GitHub will ask:

* GitHub **username**
* GitHub **Personal Access Token** (instead of password)

Generate token here:
👉 [https://github.com/settings/tokens](https://github.com/settings/tokens)

---

## 🔹 **11. Fork & Pull Request**

### **Sync fork**

```
git fetch upstream
git merge upstream/main
```

### **Create Pull Request**

You do this on GitHub UI → *Compare & Pull Request*.
