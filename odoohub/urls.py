from django.urls import path
from .views import UserLogin, UserLogout, ChangePassword, UserInfo


urlpatterns = [
    path('login', UserLogin.login),
    path('change_password/', ChangePassword.password),
    path('get_user_info/', UserInfo.get_user_info),
    path('logout', UserLogout.logout),
]
