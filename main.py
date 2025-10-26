import os
project_name = input("Whats your Project name?: ")
app_name = input("Whats your app name?: ")
git = input("Do you want to initialize a git repository? (y/n) (default: y): ").lower()

os.mkdir(project_name)
os.chdir(project_name)
if git == '':
    git = 'y'
if git == 'y':
    os.system('git init')
os.system(f"django-admin startproject {project_name}")

