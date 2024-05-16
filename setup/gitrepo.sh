#!/bin/bash

#create repo as git user
echo "Create Bare Repo as git user"
ssh git@localhost -C "git init --bare my_project.git"

#Make sure we are in labadmin home and clone repo
echo "Clone locally as labadmin"
cd
git clone ssh://git@localhost/~/my_project
cd my_project

#Add content
echo "Adding content to repo and sync"
echo "My first repo" > README
cp ~/devops/.gitignore ~/my_project
git add .
git commit -m "First Commit"
git push

#Create Virtual Environment
echo "Create Virtual Environment and requirements"
python3 -m venv ~/my_project/.venv
source ~/my_project/.venv/bin/activate
pip install pytest wheel setuptools
pip freeze > ~/my_project/requirements.txt
git add .
git commit -m "Add requirements"
git push
