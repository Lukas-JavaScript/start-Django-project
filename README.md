# 🧰 Django Project Auto-Setup Script

This Python script automates the creation of a new Django project including virtual environment setup, package installation, and optional Git initialization.

---

## 🚀 Features
- Automatically creates a clean project directory  
- Sets up a virtual environment (`.env`)  
- Installs **Django** and additional libraries of your choice  
- Initializes a **Git** repository (optional)  
- Starts a fresh Django project in the current folder 
- Adds a .gitignore file and ignores this foders: a, test 

---

## 📋 Requirements
- **Python 3.x** installed and available in PATH  
- **pip** (comes with Python)
- Optional: **Git** installed (for repository initialization)

---

## ⚙️ Usage

Run the script in a terminal:

```bash
python main.py
```
You will be asked the following:

###### 1. Project name – the name of the main Django project directory

###### 2. App name – currently not used, reserved for future features

###### 3. Git initialization – choose y or n (default: y)

###### 4. Libraries – space-separated list of additional Python packages to install

Creates a new directory and moves into it

Initializes a Git repository (if selected)

Creates a Python virtual environment (.env)

Installs Django and other libraries inside the virtual environment

Generates a new Django project in the same directory

Performs the first Git commit (if enabled)
 
#### 💡 Notes
You do not need to manually activate the virtual environment.
The script runs all commands through the environment's Python executable directly.

