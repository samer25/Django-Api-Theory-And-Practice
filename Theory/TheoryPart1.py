"""
Theory coverage part 1

-API
-REST
-Error Codes / HTTP Status Codes
-Endpoints

"""

"""
Tradition Web Paradigm
-HTTP


------------|   data     |--------------------|       |---------------------|
  Browser   | <--------- |      Webserver     |-----> |      Database       |
(Front-end) | ---------->| (Backend/Frontend) |<----- | (Weather Database)  |
------------|  Get/Post  |--------------------|       |---------------------|

Paradigm we have a browser a user opens their browser they type in a domain name
they send a request to a server that server has all the web pages stored 
on it maybe it's connected to a database it would deal with that request
and send the web page back to the browser


REST - Representation state transfer
-Rest
-Restful Web services

------------|data(JSON/XML)|--------------------|       |---------------------|
 React App  | <---------   |    RestFull API    |-----> |      Database(s)    | <----- Source
            | ---------->  |                    |<----- | (Weather Database)  |
------------|   Request    |--------------------|       |---------------------|

Thing to know about a RESTful API service is that the data that we return
from it can be utilized in any language or any platform, because the data that
we return is going to be in this generic JSON or XML format and that type of format
can be utilized by any programming language 
"""

"""
HTTP Request Methods
-GET  -PUL     -OPTIONS
-HEAD -DELETE  -TRACE
-POST -CONNECT -PATCH

HTTP protocol there's a differing amount of request methods or instructions
that we can send to the server based upon what data that we want or how
we want that data 
"""

"""
HTTP Status Response Codes
(2xx) Success
 -200 Success, 201 Crated, 202 Accepted
(3xx) Redirections
(4xx) Client Error
 -404 Not Found
(5xx) Server Error
 -500 Internal Server Error
 
Allows the web server to interact with the browser in a way that both technologies
understand the language 
So HTTP has status response codes so as it suggests status response codes are
codes that the server might send back to the browser to indicate if there's a problem or succeed the task
If the server is sending a response back it means that on our front-end we can then capture
that response and we can then do something on the front-end on the page to indicate to the user 
that it's been created (201) or something else
For example if we received a 201 response back from the server we might have something appear on the 
screen to say "Yes you have just created some data and it was successful"
It better to understand them to  better debug or test our code 
"""

"""
Applied to web servers
Restful APIs
-a base URL http://ex.com/api/
-HTTP methods (GET,POST,PUT,PATCH and DELETE)
-is stateless like HTTP
-Includes media type to define state transition  data elements (JSON)

The URL is a point of entry into the system 
so we use links like this to direct users to data 
"""

"""
When we connect to our restful api service we are going to send a request
then we are going ro receive data from our service we the make another request
and then we return some more data
So every cycle here is completely independent from the previous one and it's stateless
so  we don't remember by default anything that's happened in the previous request
so we don't store what happen previously it's a stateless protocol
This is important to remember once we start with authentication that every time we make 
a connection to our restful api we need to authenticate the user   
Every time we send or ask request data from the restful api we need to 
actually also send some sort of authentication signature to tell the server who are we are
For that there a session that remember the user and can stay logged in
The restful api traditionally doesn't store a session 
We going to build a login facility to our restful api and then we are going to store the session
to our react application 
If we don't store the state in our react application then every time
we make a request we're going to have to login again 
"""

"""
Endpoints
Webpages normally contains link to resources(http://site.com/blog)
RESTful API have Endpoints
http://site.com/api/user/1 --> get user with id=1
http://site.com/api/books -- get all books
Data is returned as (JSON etc)

Endpoints and Request Methods

RESTful API have Endpoints
- http://site.com/api/user/1
Server respond base upon request type:
-GET-retrieve user 1 data
-DELETE- delete user 1 
"""

"""
Permissions 

Permissions are very critical part of this process
There are three paces where we can add permissions
we can define a permission project wide or we can define a permission within our view.py
or can define permissions per object

Rest framework gives us an option within our project settings to define project 
level permissions 
settings.py:

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES':[
        'rest_framework.permissions.AllowAny', ---> AllowAny will allow any one access to this api
        # Permissions:
        # AllowAny
        # IsAuthenticated
        # IsAdminUser
        # IsAuthenticatedOrReadOnly
    ]
}
"""

"""
Testing with coverage

Coverage it's helps to identify what test need to be done
We have to install coverage 
pip install coverage

Then we have command that is going to check  all test
coverage run --omit='*/venv/*' manage.py test - that will skip the venv folder
point of coverage we run the command "coverage html" that will create new folder called
htmlcov  and when we open the folder and then go to index.html opened in browser will
show us what test are missing example blog/models.py and if we click on it will tell us
what test we need to run (will be market in red the lines)
"""
"""
The test of API is different we have to use(import)
from django.urls import reverse
from rest_framework import status - the status that will use if is created or etc 
from rest_framework.test import APITestCase - this is for API test case 
"""

"""
We have to install django-cors-headers
This will allows in-browser requests to your Django 
application from other origins
Adding CORS headers allows your resources to be accessed on other domains

pip install django-cors-headers

the we have to go to settings.py 
and add in INSTALLED_APPS      

'corsheaders',

then in MIDDLEWARE we have to add

"corsheaders.middleware.CorsMiddleware",

above 

"django.middleware.common.CommonMiddleware",

then we have to add variable that will allow other 
domain to access the resources will use a react

CORS_ALLOWED_ORIGINS = [
    'http://127.0.0.1:3000',
    'http://localhost:3000',

]

Now react can access the django resources 
 
"""
