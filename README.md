# StudentDoubt
set up the project by using
*sudo apt-gett install virtualenv
virtual env -p python3 env
source env/bin/activate
pip3 install  django
django-admin startproject Doubt
python manage.py startapp polls
pip install -r requirement.txt
setup you daatabase in Posgresql and create a database as StudentDoubt
python manage.py makemigrations 
python manage.py migrate
python manage.py runserver
