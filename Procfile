release: sh -c 'rails db:migrate && run rake db:schema:load && rake db:migrate --app profileuser && python manage.py makemigrations && python manage.py migrate'
web: gunicorn project_django.wsgi --log-file -
