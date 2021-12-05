## Django Instagram
Instagram clone using python django with a lot of Instagram features.

## AUTHOR 
*ROBBIN MWANGI*
[Robbin Mwangi](https://github.com/RobbinGIT)

## Features
- User authentication(Sign up and sign in).
- Password Reset using email.
- Posting Images.
- Like and comment on a post.

## Admin Dashboard

[Admin Dashboard Login](https://theinstaclone.herokuapp.com/admin/)  with credentials

### Installation
- Make sure Python is installed.
- Clone the repository and change your directory to Instagram_clone.
- Install requirements using following command.

```
pip install -r requiremnts.txt
```
### Usage
- Create a ``.env`` file.
- Declare following environment variables in the .env file.
```
> SECRET_KEY = 'secret key'
> DEBUG = True
> EMAIL_USERNAME = 'your email address'
> EMAIL_PASSWORD = 'your password' 
```
- Now make the migrations.
```
python manage.py migrate
```
- Commit the migrations.
```
python manage.py makemigrations
```
- Create a super user.
```
python manage.py createsuper
```
- Run the app.
```
python manage.py runserver
```
- Open the app at `localhost:8000` or `http://127.0.0.1:8000/`

## TECHNOLOGIES USED 
* [Python3.8](https://www.python.org/)
* [Django](https://docs.djangoproject.com)
* [Heroku](https://heroku.com)
* HTML - For building Mark Up pages/User Interface
* CSS - For Styling User Interface

## LIVE LINK
https://theinstaclone.herokuapp.com/

## Contact Me 
### RobbinGit
[Gmail](robbingithimbo@gmail.com)
[Github](https://github.com/RobbinGIT)