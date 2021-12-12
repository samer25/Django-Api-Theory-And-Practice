"""
API Documentation
Create a schema and generating API documentation automatically

Django coverage:
API Schema creation
API Documentation tools


Schema:
A schema is metadata that details how data is structured
Metadata - data about data
Machine-readable document
-API Endpoints
-URLs
-HTTP requests supported
"""

"""
Fist we have to install package called "pyyaml" which is used to generate 
the schema where we are going to use

pip install pyyaml

Now we have to add it to urls in our project first we have to import it

from rest_framework.schemas import get_schema_view

path('schema/', get_schema_view(
    title='BlogAPI',
    description='API for BlogAPI',
    version='1.0.0'
    ), name='schema'),
    
Now we have to install OpenAPI this package is going to help
the schema to develop the schema and get all the different 
urls here that are required to build the schema 

pip install uritemplate

now when we go to browser and time /schema will have it 
we will see some path and show us all the parameters 
all the attributes all the settings of the particular path or the endpoints 
"""

"""
Doc Generator for Django REST Framework(options)

Django REST Swagger
Swagger-ui
drf-yasg
Redoc

Those are different packages that's going to essentially take a
schema and put it into a nice interface that we can interact with

we weill use first coreAPI

first we going to import from rest_framework documentations
in project/urls.py

from rest_framework.documentation import include_docs_urls

path('docs/', include_docs_urls(title='BlogAPI')),

now we have to implement the coreAPI 
to get coreAPI start we can add it to REST_FRAMEWORK and create the default schema class in the settings.py

REST_FRAMEWORK = {'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema' }

then will install coreapi

pip install coreapi

now when we go to browser and go to docs/ will se graphical interface for
our schema and we can interact with endpoints
"""