from django.urls import path
from tasks import views


urlpatterns = [
    path('', views.index),
    path('users/', views.users),
    path('login/', views.login),
    path('users/create/', views.create),
    # http://127.0.0.1:8000/users/create/
    
]