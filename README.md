# easyrest
A simple rest api built with Django

the html files have a javascript interface to the api that allows users
to interact with a chatbot, powered by the API. This JavaScript is the only
thing that will need to be deployed.

Requirements to run:
1. python 3.7
2. virtualenvwrapper
3. Once those are installed, create a virtual environment with
    mkvirtualenv <environment name>
    workon <environment name>
4. You should now be in your environment, run the following command to install the requirements
  pip install -r requirements.txt
5. Once all the requirements are installed, you can run the app with the command  
  manage.py runserver
6. Now the API should be available to use via the html and JavaScript. You may need
  to enter a different port in the URL variable.
