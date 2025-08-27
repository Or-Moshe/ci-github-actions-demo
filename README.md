# ci-github-actions-demo
assignment 7 for devops course

# basic workflow
this worklow uses ubuntu-latest runner
steps: 
• checking out the code  
• print a simple message  
• setting up python version 3.9  
• install dependencies  
• run tests

# cron scheduling workflow
this worklow uses ubuntu-latest runner and runs every midnight UTC  
steps: 
• checking out the code  
• print a simple message  

# matrix workflow
this worklow uses ubuntu-latest runner and a matrix strategy to execute to action for each python versions: [3.7, 3.8, 3.9, 3.10] and os: [ubuntu-latest, windows-latest]
for each job:
steps: 
• checking out the code  
• print a simple message  
• setting up python version   
• install dependencies  
• run tests
