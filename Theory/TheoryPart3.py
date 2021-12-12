"""
Django coverage

JWT Process
Configure Django RESTful API

JSON Web Token

Simple JWT provides a JSON Web Token authentication backend for the Django REST Framework.
It aims to cover the most common use cases of JWTs by offering a conservative set of default features.
It also aims to be easily extensible in case a desired feature is not present.

Access Token
-Short Expiry 10/20 min.
Refresh Token
-Longer expiry 10 days


Encoded
That will look the token:
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c

Decoded will have value like this:
{
  "sub": "1234567890",
  "name": "John Doe",
  "iat": 1516239022
}
and more ...
"""
"""
Installing JWT

pip install djangorestframework-simplejwt


the in the setting we have to setup authentication in REST_FRAMEWORK

REST_FRAMEWORK = {
    .......
    'DEFAULT_AUTHENTICATION_CLASSES': (
        ......
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )

}

then we have to setup the url 
in project urls.py:

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

 path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
 path('api/token/refresh/, TokenRefreshView.as_view(), name='token_refresh')
"""
"""
Will crate custom user module that except email for user(login)
first will create new app users 
python manage.py startapp users  

then in models.py

from django.contrib.auth.models import BaseUserManager, PermissionsMixin, AbstractBaseUser
from django.utils import timezone


class CustomAccountManager(BaseUserManager):

    def create_superuser(self, email, user_name, first_name, password, **other_fields):

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True'
            )
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True'
            )

        return self.create_user(email, user_name, first_name, password, **other_fields)

    def create_user(self, email, user_name, first_name, password, **other_fields):
        if not email:
            raise ValueError('You must provide an email address')

        email = self.normalize_email(email)
        user = self.model(email=email, user_name=user_name, first_name=first_name, **other_fields)
        user.set_password(password)
        user.save()
        return user


class NewUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField('email address', unique=True)
    user_name = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=150, blank=True)
    start_date = models.DateTimeField(default=timezone.now)
    about = models.TextField('about', max_length=500, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = CustomAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name', 'first_name']

    def __str__(self):
        return self.user_name


and we have to register and add to INSTALLED_APPS the new model user in settings.py 

AUTH_USER_MODEL = 'users.NewUser'

then you have to change ForeignKey that is set to old models User to set it to the NewUser model
and delete the old database 

then makemigrations 
and migrate 

let add in the settings.py configuration for JWT

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=5),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': True,
    'UPDATE_LAST_LOGIN': False,

    'ALGORITHM': 'HS256',
    'SIGNING_KEY': settings.SECRET_KEY,
    'VERIFYING_KEY': None,
    'AUDIENCE': None,
    'ISSUER': None,
    'JWK_URL': None,
    'LEEWAY': 0,

    'AUTH_HEADER_TYPES': ('Bearer',),
    'AUTH_HEADER_NAME': 'HTTP_AUTHORIZATION',
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',
    'USER_AUTHENTICATION_RULE': 'rest_framework_simplejwt.authentication.default_user_authentication_rule',

    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',

    'JTI_CLAIM': 'jti',

    'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
    'SLIDING_TOKEN_LIFETIME': timedelta(minutes=5),
    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),
}

Now let create custom registration

in user lets create serializer.py

from rest_framework import serializers

from users.models import NewUser


class RegisterUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewUser
        fields = ('email', 'user_name', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
        
then in view.py

from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from users.serializers import RegisterUserSerializer


class CustomUserCreate(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        req_serializer = RegisterUserSerializer(data=request.data)
        if req_serializer.is_valid():
            new_user = req_serializer.save()
            if new_user:
                return Response(status=status.HTTP_201_CREATED)
        return Response(req_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


lets create urls.py in users 

from django.urls import path

from users.views import CustomUserCreate

app_name = 'users'

urlpatterns = [
    path('register/', CustomUserCreate.as_view(), name='create_user')
]

then to include in the project/urls.py

path('api/users/', include('users.urls', namespace='users'))


then we can tested in postman to create user when we write custom json
 
 {
    "email": "as@as.com",
    "user_name": "aaaa",
    "password": "A239676a"
}

and sent with POST in http://127.0.0.1:8000/api/users/register/

the result can see it in admin panel section New users
"""
"""
Now we have to deal with logout that the refresh token to go to blacklist that can be used again from somebody

In the settings.py the SIMPLY_JWT the 'BLACKLIST_AFTER_ROTATION': True have to be True
and in INSTALLED_APPS have to add 'rest_framework_simplejwt.token_blacklist'


then migrate and in admin panel will show section TOKEN BLACKLIST WITH Blacklisted token and Outstanding tokens

Now we have to create view for BlacklistTokenView

first have to import RefreshToken 

from rest_framework_simplejwt.tokens import RefreshToken

then create a View

class BlacklistTokenView(APIView):
    permission_classes = [AllowAny]
    
    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
        except = Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)  
            
            
now we have to added to users/urls.py      

path('logout/blacklist/', BlacklistTokenView.as_view(), name='blacklist')

after creating component in react for logout the refresh token will go to blacklist token
"""