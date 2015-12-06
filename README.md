# ForThePeople

To run:

virtualenv env
source env/bin/activate

pip install django
pip install djangorestframework
pip install pigments

cd ForThePeople

--> change mysql settings in forthepeople/settings.py

python manage.py migrate

python manage.py runserver


