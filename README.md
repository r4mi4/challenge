
# Challenge 2

Technologies used in this challenge:

    1- JWT
    2- Postgress
    3- DRF
    4- Docker
    5- Authorization And Authentication - JWT

## How install and run ?
```bash
$ git https://github.com/r4mi4/challenge.git
$ cd Challenge_2
```
##### Run :
```bash
$ docker-compose up -d
```
if you want to create super user :
```bash
# get container_id
$ docker ps -aqf "name=app"
$ docker exec -it container_id python manage.py createsuperuser
```
# Challenge 3

Technologies used in this challenge:

    1- HTTP Headers
    2- Postgress
    3- DRF 
    4- Docker 
    5- Rate limit 
    6- Authorization And Authentication 

## How install and run ?
```bash
$ git https://github.com/r4mi4/challenge.git
$ cd Challenge_3
```
##### Run :
```bash
$ docker-compose up -d
```
if you want to create super user :
```bash
# get container_id
$ docker ps -aqf "name=app"
$ docker exec -it container_id python manage.py createsuperuser
```


### Open ``localhost`` in your browser.