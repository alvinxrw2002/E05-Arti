release: sh -c 'heroku run rake db:schema:load && heroku run rake db:migrate --app myApp && heroku run python manage.py makemigrations && python manage.py migrate'
web: gunicorn project_django.wsgi --log-file -
