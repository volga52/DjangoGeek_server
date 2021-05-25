from django.urls import path

from adminapp.views import index, admin_user_read


app_name = 'adminapp'

urlpatterns = [
    path('', index, name='index'),
    path('admin-users-read/', admin_user_read, name='admin_users_read'),
]
