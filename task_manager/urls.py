from django.contrib import admin
from django.urls import path, include
from task_manager import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    # path('', views.TaskManagerHome.as_view(), name='home'),
    # path('login/', views.login_user, name='login'), # path('login/', views.login),
    path('login/', views.LoginUser.as_view(), name='login'),  # path('login/', views.login),
    path('tasks/', include('task_manager.tasks.urls')),
    path('users/', include('task_manager.users.urls', namespace='users')),
    path('statuses/', include('task_manager.statuses.urls')),
    path('labels/', include('task_manager.labels.urls')),
    path('logout/', views.LogoutUser.as_view(), name='logout'),
    
]
