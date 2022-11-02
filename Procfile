release: sh -c 'heroku run rake db:migrate --app myApp && python manage.py migrate'
web: gunicorn project_django.wsgi --log-file -
