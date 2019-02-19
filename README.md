# IVS project 2 - Kalkulačka
## Info
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur porttitor odio metus, et tincidunt enim viverra et. Donec egestas pellentesque neque sit amet lobortis. Nulla facilisi. Etiam ultrices molestie mauris. Vestibulum dignissim augue sit amet nisi efficitur, a gravida lorem tincidunt.

## Practicies
### Branches:
<b>master</b>  - branch pre finálne verzie bez bugov  
<b>develop</b> - branch pre development, najviac sa bude pracovať tu  
<b>feature_*</b>  - branche pre nové features, ktoré keď budú dokončené budú pushnuté do develop  

## Prerequisities
### Linux (Debian-based, e.g. Ubuntu)  
```
sudo apt-get install python3
```
### Windows  
[Download Python3](https://www.python.org/downloads/)  
## Basics
### Getting repository
<b>Over SSH:</b>
```
git clone git@github.com:adokitkat/IVS_project2.git
```
<b>Over HTTPS:</b> _recommended_ 
```
git clone https://github.com/adokitkat/IVS_project2.git
```
### Working with repo
<b>!!!</b> Switch to <b>develop</b> branch: <b>!!!</b> 
```
git checkout develop
```  
### Working on a new feature
```
git branch feature_[name of feature]    // creates a new branch
git checkout feature_[name of feature]
```
 
## From this point do everytime
Update working history:
```
git fetch
```
If changes have been made:
```
git pull
```
### After making changes in files -> uploading
```
git add .                                           // adds all new files
git commit -m"[descriptive message of the change]"
git push                                            // pushes everything from your local files to this branch
```

## Cheat-sheet pre neveriacich Tomášov
https://services.github.com/on-demand/downloads/github-git-cheat-sheet/
