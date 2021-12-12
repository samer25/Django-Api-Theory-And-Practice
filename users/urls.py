from django.urls import path

from users.views import CustomUserCreate  # ,  BlacklistTokenView # blacklist of simplejw

app_name = 'users'

urlpatterns = [
    path('register/', CustomUserCreate.as_view(), name='create_user'),
    # path('logout/blacklist/', BlacklistTokenView.as_view(), name='blacklist') # view using blacklist of simplejwt

]
