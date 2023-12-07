from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

app_name = 'account'

urlpatterns = [
    # custom login url
    # path(route='login/', view=views.user_login, name='login'),

    # use django's authentication framework
    path(route='login/', view=auth_views.LoginView.as_view(), name='login'),
    path(route='logout/', view=auth_views.LogoutView.as_view(), name='logout'),
    path(route='', view=views.dashboard, name='dashboard'),
]
