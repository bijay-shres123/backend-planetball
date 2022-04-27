# project
The project is created as per requierments for coursework under SOFT7003. This work belongs to Group 3.

The first thing to do is to clone the repository:

$ git clone https://github.com/gocardless/backend-planetball.git
$ cd backend-planetball
Create a virtual environment to install dependencies in and activate it:

$ virtualenv2 --no-site-packages env
$ source env/bin/activate
Then install the dependencies:

(env)$ pip install -r requirements.txt
Note the (env) in front of the prompt. This indicates that this terminal session operates in a virtual environment set up by virtualenv2.

Once pip has finished downloading the dependencies:

(env)$ cd project
(env)$ python manage.py runserver
And navigate to http://127.0.0.1:8000/backend-planetball/.

In order to test the purchase flows, fill in the account details in project/gc_app/views.py to match your SANDBOX developer credentials.

