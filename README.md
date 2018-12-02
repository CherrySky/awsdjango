# About this project
 AWS EC2
 - virtualenv
 
 Local
 - anacoda 
 - pycharm
 - git
 - django

# Environment setup in Aws EC2
1. sudo yum list | grep python3
2. python3 get-pip.py --user
3. pip install awsebcli --upgrade --user
4. eb --version
5. pip install --user virtualenv
6. virtualenv -p /usr/bin/python3 ~/eb-virt
7. source ~/eb-virt/bin/activate
8. pip install django==2.1.1
9. pip freeze
10. django-admin startproject <website-name>

# How to start up django server in EC2 background
1. screen
2. python manage.py runserver 0.0.0.0:8000
- use Ctrl+A ->> d to exit
- you need to add EC2 hostname into settings.py > ALLOWED_HOSTS