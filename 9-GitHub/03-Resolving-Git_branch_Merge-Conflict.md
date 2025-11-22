## **What is a Merge Conflict?**

A **merge conflict** happens when two branches change the same line of a file, or when one branch edits a file that the other branch deletes.

Git cannot decide which version to keep, so **you must choose manually**.

---

## **Where Merge Conflicts Occur**

You will see conflicts when running:

```
git merge branchname
```

or

```
git pull
```

Example:

```
Auto-merging index.html
CONFLICT (content): Merge conflict in index.html
Automatic merge failed; fix conflicts and commit the result.
```

---

## **How to Resolve a Merge Conflict**

## **Step 1: Open the file causing conflict**

Inside the file, Git marks the conflicting code like this:

```
<<<<<<< HEAD
Your current branch code (main)
=======
Code from the branch you are merging (feature)
>>>>>>> feature
```

---

## **Step 2: Choose one of the versions (or combine both)**

### Option A: Keep your branch version

Delete everything except:

```
Your current branch code
```

### Option B: Keep incoming (other branch) version

Delete everything except:

```
Code from the branch you are merging
```

### Option C: Combine both changes

You can manually merge and keep both parts.

---

## **Step 3: Remove conflict markers**

Delete:

```
<<<<<<<
=======
>>>>>>>
```

Keep only the final resolved code.

---

## **Step 4: Add resolved file to staging**

```
git add filename
```

---

## **Step 5: Commit the merge**

```
git commit -m "Resolved merge conflict"
```

If conflict occurred during `git pull`, it will continue after this commit.

---

## **Example of Resolving a Conflict**

### Conflict:

```
<<<<<<< HEAD
title = "Machine Learning Notes"
=======
title = "ML Notes - Updated"
>>>>>>> feature-update
```

### Resolved version:

```
title = "Machine Learning Notes (Updated)"
```

Then:

```
git add notes.txt
git commit -m "Resolved conflict in notes.txt"
```

---

## **Useful Commands During Conflict**

### **See which files have conflicts**

```
git status
```

### **Abort merge (go back to original state)**

```
git merge --abort
```

### **View conflict details**

```
git diff
```

---

## **Best Practices to Avoid Merge Conflicts**

✔ Pull latest changes before working

✔ Commit frequently

✔ Use smaller branches

✔ Communicate with teammates

✔ Avoid editing same lines in a file


