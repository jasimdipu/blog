# blog - a who django project assignment
## Instructions

NOTE: you must install docker on your working machine

### Project link
```
https://github.com/jasimdipu/blog.git
```
# Project Installation
download the project first, then change the directory to blog.
if you have mysql database installation make sure the mysql database is running on
your machine. Then create database. please note down the database name, user and password.
After that create a .env file and copy and paste the resources from .env.example. Make changes the 
database credentials.
```
SECRET_KEY="secret-key"
DEBUG=Debug
ALLOWED_HOSTS=Allowed_host

DB_ENGINE=DB_ENGINE
DB_HOST=DB_HOST
DB_PORT=DB_PORT
DB_NAME=DB_NAME
DB_USER=DB_USER
DB_PASSWORD=DB_PASSWORD

CORS_ALLOWED_ORIGINS=CORS_LIST
```
Make sure you have a secret key of your project, you can make it on the online using this link in bellow
```
https://djecrety.ir/
```
make the debug false and add host address which is your domain address and add the address on **CORS_ALLOWED_ORIGINS** which you are allowed 
for your api.

### Docker 
Please make sure you are on the root folder. User docker command for database migrations and project run
```
docker-compose up -d --build
```
### Run and Test on Web

For test the project use 
```
http://localhost:8000/api/v1/schema/swagger-ui/
```
and you are found the api schemas in bellow





