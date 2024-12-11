from django.urls import path
from task_manager.users import views


app_name = 'users'
urlpatterns = [
    path('', views.users, name='home'),
    path('create/', views.UsersCreate.as_view(),
         name='create'),
    path('<int:user_id>/update/', views.UsersUpdate.as_view(),
         name='update'),
    path('<int:user_id>/delete/', views.UserDelete.as_view(),
         name='delete'),
]
