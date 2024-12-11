from django.contrib import admin
from django.urls import include, path
from task_manager import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index,
         name='home'),
    path('login/', views.LoginUser.as_view(),
         name='login'),
    path('tasks/', include('task_manager.tasks.urls')),
    path('users/', include('task_manager.users.urls',
                           namespace='users')),
    path('statuses/', include('task_manager.statuses.urls')),
    path('labels/', include('task_manager.labels.urls')),
    path('logout/', views.LogoutUser.as_view(),
         name='logout'),
]
