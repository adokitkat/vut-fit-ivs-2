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
<b>Over HTTPS:</b>
```
git clone https://github.com/adokitkat/IVS_project2.git
```
### Working with repo
<b>!!!</b> Switch to <b>develop</b> branch: <b>!!!</b> 
```
git checkout develop
```
Update working history:
```
git fetch .
```
If changes have been made:
```
git pull
```
### Making changes
```
git commit -m"[descriptive message]"
git push .                               // == git push everyhing in this branch <- git push [remote] [branch]
```

