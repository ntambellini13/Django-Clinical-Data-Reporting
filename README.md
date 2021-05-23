# Django-Clinical-Data-Reporting
Very basic styling and validation, focus is on implementing different parts of Django including
Forms, Views, Templates

1) Create your mysql image using the following command
2) docker run -d -p 6666:3306 --name=docker-mysql --env="MYSQL_ROOT_PASSWORD=mypassword" --env="MYSQL_DATABASE=mydb" mysql --default-authentication-plugin=mysql_native_password
3) Then build dockerfile using:
    docker build -f Dockerfile -t clinical_data_app .
5) link docker-mysql to docker image using:
    docker run -t --name=clinicals-app --link docker-mysql:mysql -p 10555:8000 clinicals_app
5) Apply migration if needed using:
    docker exec -it clinicals-app python manage.py migrate
6) Access/run the application locally using - http://localhost:10555 

