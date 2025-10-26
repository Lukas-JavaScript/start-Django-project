import os
import shutil as sh
import subprocess

# === Eingaben ===
project_name = input("What's your project name?: ").strip()
app_name = input("What's your app name?: ").strip()
git_input = input("Do you want to initialize a git repository? (y/n) (default: y): ").lower().strip()

# === Projektordner vorbereiten ===
if os.path.exists(project_name):
    sh.rmtree(project_name)

os.mkdir(project_name)
os.chdir(project_name)

# === Git vorbereiten ===
git = (git_input == '' or git_input == 'y')
if git:
    subprocess.run(["git", "init"])

# === Virtuelle Umgebung ===
subprocess.run(["python", "-m", "venv", ".env"])

# Pfad zur Python-Exe in der venv
venv_python = ".env\\Scripts\\python.exe" if os.name == "nt" else ".env/bin/python"

# === Pakete installieren ===
subprocess.run([venv_python, "-m", "pip", "install", "--upgrade", "pip"])
subprocess.run([venv_python, "-m", "pip", "install", "django", "django-cors-headers", "requests"])

# === Django-Projekt erstellen ===
subprocess.run([venv_python, "-m", "django", "startproject", project_name, "."])

# === Optional: Git commit ===
if git:
    subprocess.run(["git", "add", "."])
    subprocess.run(["git", "commit", "-m", "start Django project"])

print(f"\n✅ Django project '{project_name}' was created successfully.")
print(f"👉 Virtual environment: {os.path.abspath('.env')}")
print(f"👉 Start the server with:\n    {venv_python} manage.py runserver")
