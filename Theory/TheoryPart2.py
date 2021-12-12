"""
Django coverage:

Project level permissions
Django users/ group permissions
View level permissions
Object level permissions
Developing custom permissions
"""

"""
Permission levels
We can apply permissions:
-Project-level
-View-level
-Object-level
"""

"""
Project level permission

This is apply in whole system
settings.py:

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES':[
        'rest_framework.permissions.AllowAny', ---> AllowAny will allow any one access to this api
    ]
}

There are different settings that can apply:
AllowAny
IsAuthenticated - require anyone who tries to access the restful api data 
                    they have to be authenticated(like sign in/ logged in )
IsAdminUser - Have to be admin user / superuser
IsAuthenticatedOrReadOnly - have to be authenticated or not can read only

"""

"""
View level:

We have to import the permission from rest_framework

from rest_framework.permissions import IsAdminUser
then in class view we can apply permission with permission_classes = [IsAminUser]

there are DjangoModelPermissionsOrAnonReadOnly - the new user can view and add data and non user can only ready a data
"""
"""
When we create new user and is not admin we can login for that in project urls we add
new path

path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))

That will allow us simulate a user logging

and now when you go to browser in /api will show top left Log in and can login/logout

"""

"""
Now lets make connection between permissions and http request

Permissions -> HTTP Request
Permissions:
-View -> GET
-Delete -> DELETE
-Change -> PUT, PATCH
-Add -> POST

Let build custom permission

Imagine we have the blog table  users make a new entry or new post in the blog 
so the only person should be able to access in terms of editing and deleting 
that particular post is the person who made that post
So create new class and  import the class BasePermission from rest_framework.permissions

class PostUserWritePermission(BasePermission):
    message = 'Editing posts is restricted to the author only.'
    
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS: # if the methods GET HEAD or OPTIONS is in SAFE_METHODS
            return True  # we return true and the user can view the data only
        
        return obj.author == request.user  # that will check if the obj is the user object(author is from the model post)


Now we can apply it in the class PostDetail view

class PostDetail(generics.RetrieveAPIView, PostUserWritePermission):
    permission_classes = [PostUserWritePermission]

"""