# ec-shop-django

#Active ENV
env/Scripts/activate

#Run server

python manage.py runserver

#After static folder create and store data run

python manage.py collectstatic

#Make migration
python manage.py makemigrations

#Before run migration install pillow
pip install Pillow

#Migrate file
python manage.py migrate

#Create Super User
python manage.py createsuperuser
