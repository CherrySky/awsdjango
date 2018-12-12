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

# How to install channels in Window
1. (installed anaconda, in env) conda install -c conda-forge scrapy 
2. pip install -U channels
3. pip install channels_redis

# How to install channels in Linux
1. sudo apt-get install python3 python3-dev
2. (inside virtualenv) pip install scrapy
3. pip install -U channels
4. pip install channels_redis

# How to run redis-server in Window?
1. unzip redis64-2.6.12.1.zip (need redis.py version 2)
2. redis-server.exe
