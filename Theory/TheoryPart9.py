"""
Django DRF -Social Authentications

Look at the underpinning steps to implement Social Authentication
with Django Rest

Django Coverage

Social Authentication Work-flow
Implement the Django Restful API Back-end
"""


"""
JWT workflow recap
----------------------

----------------| POST Login Request        |----------------------     
                |----------------------->   |
                |Access and Refresh Token   |   
                |<-----------------------   |
                |     HTTP request          |
                |------------------------>  |
 Browse/website |     JWT Auth Needed       |
                |<------------------------  |
                |Request + Access Token     |   RESTful API  
                |------------------------>  |
                |    Token Expired          |
                |<------------------------  |
                |      Refresh Token        |
                |------------------------>  |
                |     New Token             |
                |<------------------------  |
                | Request + Access Token    |
                |------------------------>  |-----------------------
----------------|



Social login workflow
--------------------------
Social Login Process

          Link to login (new windows) 
|--------| -------------------------------> |-----------|
|        |OAuth2 provider - (Access Token)  |  FaceBook |
|        |<-------------------------------- |-----------|
|        |                                   |up     |down
|        | Login Request (Access Token)      |       |   ------>  Check Access Token
| Website| ------------------------------->|-------------|        return user details
|        | Return Access and Refresh Token |             |   
|        | <------------------------------ | Restful API |
|        |  Data request(Access Token)     |             |
|--------|  -----------------------------> |-------------|


Removing SimpleJWT
--------------------
first we need to strip out simplejwt from this project 
because we will use  of2 provider service that we installed

first go to project/urls.py 
and remove the imports form rest_framework_simplejwt.views ...
and the urls paths 
then go to settings.py and remove 
blacklist from installed apps
and remove SIMPLE_JWT 
and in the default_authentication_classes remove
    the simplejwt authentication

then in user views.py and urls.py we have the Blacklist when we are using
JWT tokens we have to remove it 
in users.py we have to remove the class BlacklistTokenView and the imports
and in user/urls.py we have to remove the path(logout/blacklist .. . .)

Installing drf social oauth2 package
---------------------------------------
Now we have to install multiple packages
first we are going to install 

pip install drf_social_oauth2

after we install drf_social_oauth2

lets adds in settings.py INSTALLED_APPS those apps

'oauth2_provider',
'social_django',
'drf_social_oauth2',

then migrate to apply the changes

now in admin panel will have section 
DJANGO OAUTH TOOLKIT with 
Access tokens,
Applications
Grants
Refresh tokens

this will manage our access and refresh tokens
and addition to that going to allow us to create
an applications 
this package requires us to build an application
and we essentially we log in through that application
We can check the application setting by going
to create new application in section 
DJANGO OAUTH TOOLKIT/Applications

And section 
PYTHON SOCIAL AUTH with
Associations
Nonces
Use social auths

this will going to manage all the users that are 
logged in via social authentication

Integrate drf-social-oauth2 and token management
----------------------------------------------

then we need a setup the urls.py
in project/urls.py
add the path

path('auth/', include('drf_social_oauth2.urls', namespace='drf')),

we need to be careful if we need to put this path in other app urls
because the namespace may be different and that potentially cause issues
we will called all the urls and access it trough the namespace

now if we go to /auth/ will show page not found 
but will see all the urls of auth/ that we need 
if we add one of the path for example
/auth/token we can access to the endpoint
that is to check if it work

now we have to go to settings.py and add in
TEMPLATES = [
    {
        ....
        ....
        'OPTIONS: {
            'context_processors':[
                ......
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ]       
        }
    }
]

this is going to make these services of these packages available
throughout whole project by adding it 

after that we have to add IN DEFAULT_AUTHENTICATION_CLASSES'=() the 

    'oauth2_provider.contrib.rest_framework.OAuth2Authentication',
    'drf_social_oauth2.authentication.SocialAuthentication',

and now again in settings.py we have to add
AUTHENTICATION_BACKENDS = (
    'drf_social_oauth2.backends.DjangoOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)

this mean that these are the methods these are a ways
that we can authenticate in this system

by looking in at the second one means that we still using django backend so
we can log in into admin but now and the first one we 
can also use drf social oauth2  that is the package that we installed



The package django-oauth-toolkit will help us to provide jwt
token and manage it 
and the 
python-social-auth - that will help us to make the connections
to facebook and google etc.
and the package that we install drf-social-oauth2 is a glue 
to wrap these two packages is providing additional features
 that we can authenticate from an api and then it's going to 
 hook into these other packages and then allow us the 
 social authentication and allow us the jwt token that we are 
 going to be generating 


Testing Stage one CURL - setting up tokens
--------------------------------------------------
That is the setup! Now we can generating tokens 
Lets test it in terminal using Curl

Retrieve a token for a user using curl:

curl -X POST -d "client_id=<client_id>&client_secret=<client_secret>&grant_type=password&username=<user_name>&password=<password>" http://localhost:8000/auth/token


Now lets test it in postman 
we have to create application in admin panel at section 
DJANGO OAUTH TOOLKIT

the sections that need to fulfill are:

User = 1 or existed user id 
client type = Confidential
Authorization grant type =  Resource owner password-based


after we create application we have 
Client_id at the top and the bottom we have client secret
we will need this for testing 

in postman
url section : http://127.0.0.1:8000/auth/token
at body we have to select x-www-form-urlencoded
and in key will add needed information
username 
password
grant_type
client_secret
client_id
then in value front of keys
email count
the password of the account
password(just the word not actual password)
secret key (from DJANGO OAUTH TOOLKIT/application in admin panel)
client id (from DJANGO OAUTH TOOLKIT/application in admin panel)

now can send the POST and we will access some data like:

{
    "access_token": "MIrbfG8WvSdI4CyjEn31Rmr9sNw5T3",
    "expires_in": 36000,
    "token_type": "Bearer",
    "scope": "read write",
    "refresh_token": "46Tj3hlUWApgHTB8a7uEejAJIT5rbI"
}
that mean it working

in views we have to put permission_classes in the classes where we need


Now we can focus on Social Login
Configuring Facebook social login
----------------------------------------------

To use Facebook as the authentication backend of our REST API in settings.py
we have to overwrite the AUTHENTICATION_BACKENDS

AUTHENTICATION_BACKENDS = (
    # Others auth providers (e.g. Google, OpenId, etc)
    ...

    # Facebook OAuth2
    'social_core.backends.facebook.FacebookAppOAuth2',
    'social_core.backends.facebook.FacebookOAuth2',

    # drf_social_oauth2
    'drf_social_oauth2.backends.DjangoOAuth2',

    # Django
    'django.contrib.auth.backends.ModelBackend',
)

# Facebook configuration
SOCIAL_AUTH_FACEBOOK_KEY = '<your app id goes here>'
SOCIAL_AUTH_FACEBOOK_SECRET = '<your app secret goes here>'

we have to go in browser to FACEBOOK for Developers and register then
create new app after that will see a dashboard we have to go in settings
and copy the App ID and past it in SOCIAL_AUTH_FACEBOOK_KEY
also we need to copy a App Secret also in settings 
and past it in SOCIAL_AUTH_FACEBOOK_SECRET

# Define SOCIAL_AUTH_FACEBOOK_SCOPE to get extra permissions from Facebook.
# Email is not sent by default, to get it, you must request the email permission.
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']
SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {
    'fields': 'id, name, email'
}

Now that everything is set up we can perform login requests from Frontend
More for setting up social login in : https://github.com/wagnerdelima/drf-social-oauth2

When we are sending a request may be we will have an error because we have created
custom user and the problem is that user model doesn't match the data
that's been returned  from facebook so we need to kind of mach up the user
data that's being sent back from facebook to create a new user in this system
(if we use the default user model then everything will be fine)
So one of the option we have  if we go into the project/settings.py
and add SOCIAL_AUTH_USER_FIELDS variable we can define the "email , username, first_name, password"

SOCIAL_AUTH_USER_FIELDS = ['email', 'username', 'first_name', 'password'] 

and that matches up with our user table
"""