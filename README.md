# CarZen - WebApp

## AI powered Car servicing medium

An app that helps connecting Car oweners and Car Serviceing offering companies


## FEATURES:

 - CarZen can create and keep track of car servicing

 - Service offering companies are rated by their clients

 - Reviews pass through sentiment analysis to generate final rating



 - Car owners can search nearby servicing offers

 - Select the best fit service for their domain of required work

 - Book appointments



## Keep track of:

 - billings

 - their cars' servicing history

 - amount spent on each car

 - parts replaced



## Have more on your mind?

Checkout a branch now and start coding :)





## Installation guide:
- Clone the repo
- Setup python
- Install pip and django 3.0
- create virtual enviornment
- run the following in terminal:
```
pip install -r requirements.txt
```
- Create and host mySQL DB on local or any hosting service
- add database host and credentials in BI/settings.py file
- run the following in terminal:
```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver <port to run on>
```
Its live! hit http://127.0.0.1:port/
