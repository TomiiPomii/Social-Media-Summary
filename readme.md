# Social Media Summary

The goal of this project is to provide a overview of a social media user. Enter the url to a user profile to get information about this user.

## How to develope

You need to have docker installed on your system.

1. Download this repository
2. cd into the projects root directory
3. create a .env file in the root directory
4. add the following environment variables to the file

```shell
DJANGO_SECRET_KEY=<YOUR_DJANGO_SECRET_KEY>
DJANGO_ALLOWED_HOSTS=*
DJANGO_DEBUG=True
POSTGRES_PASSWORD=password
POSTGRES_USER=postgres
TWITTER_CONSUMER_KEY=<YOUR KEY>
TWITTER_CONSUMER_SECRET=<YOUR SECRET>
TWITTER_ACCESS_TOKEN_KEY=<YOUR KEY>
TWITTER_ACCESS_TOKEN_SECRET=<YOUR SECRET>
```

5. Build and run the containers

```shell
docker-compose build
docker-compose up
```

6. make migrations and create superuser

```shell
docker-compose exec web python manage.py makemigrations
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
```

7. test if everything works correctly

```shell
docker-compose exec web python manage.py test
```

## How to deploy

This project is ready to be deployed to heroku. Follow the steps below to deploy your own version. You first have to install [the heroku CLI](https://devcenter.heroku.com/articles/heroku-cli#download-and-install).

1. Login and create your app

```shell
heroku login
heroku create <app_name>
heroku stack:set container --app=<app_name>
```

2. Connect your app with your git repository

```shell
heroku git:remote -a <app_name>
git checkout deploy
git push heroku deploy:master
heroku addons:create heroku-postgresql:hobby-dev
```

3. After the image is build run the following commands:

```shell
heroku run python manage.py migrate
heroku run python manage.py createsuperuser
```

4. Your app is now online here: https://<app_name>.herokuapp.com/
