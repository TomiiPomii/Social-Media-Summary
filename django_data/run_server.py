import os

if (os.environ.get("DJANGO_DEBUG") == "True"):
    print("Run server in development mode")
    os.system("python manage.py runserver 0.0.0.0:8000")
else:
    print("Run server in production mode")
    os.system("gunicorn django_project.wsgi:application --bind 0.0.0.0:8000")
