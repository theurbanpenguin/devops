#!/bin/bash

ssh git@localhost -C "git init --bare my_project.git"

cd

git clone ssh://git@localhost/~/my_project

cd my_project

echo "My first repo" > README
cp ~/devops/.gitignore ~/my_project
git add .
git commit -m "First Commit"
git push

python3 -m venv ~/my_project/.venv
source ~/my_project/.venv/bin/activate
pip install pytest wheel setuptools
pip freeze > ~/my_project/requirements.txt

git add .
git commit -m "Add requirements"