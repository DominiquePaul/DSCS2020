# file used in class to demonstrate a git merge

mkdir gittest
cd gittest

git init

vi test.py

python:
--------------
import random

random.random()
--------------

git add .
git commit -m "added file"

git branch feature1
git checkout feature1

vi test.py

python:
--------------
import random

x = random.random()
--------------


git add .
git commit -m "made some changes"

git checkout master
vi test.py

python:
--------------
import random

y = random.random()
--------------
git add .
git commit -m "made some other changes"


git merge feature1

vi test.py

git add .
git commit -m "merged with feature1"



# For creating a new branch out of an older commit

git log

git branch new_branch <hash>

git checkout new_branch
