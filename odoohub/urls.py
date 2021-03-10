from django.urls import path

from . import views

urlpatterns = [
    path('login', views.user_login),
    path('change_password/', views.change_password),
    path('get_user_info/', views.get_info),
    path('logout', views.login_logout),
]
