from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views

from . import views

app_name = 'account'

urlpatterns = [
    # custom login url
    # path(route='login/', view=views.user_login, name='login'),

    # use django's authentication framework
    # login / logout urls
    path(route='login/', view=auth_views.LoginView.as_view(), name='login'),
    path(route='logout/', view=auth_views.LogoutView.as_view(), name='logout'),

    # change password urls
    path(route='password-change/',
         view=auth_views.PasswordChangeView.as_view(success_url=reverse_lazy('account:password_change_done')), name='password_change'),
    path(route='password-change/done/',
         view=auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),

    # reset password
    path(route='password-reset/',
         view=auth_views.PasswordResetView.as_view(success_url=reverse_lazy('account:password_reset_done')), name='password_reset'),
    path(route='password-reset/done/',
         view=auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path(route='password-reset/<uidb64>/<token>/',
         view=auth_views.PasswordResetConfirmView.as_view(success_url=reverse_lazy('account:password_reset_complete')), name='password_reset_confirm'),
    path(route='password-reset/complete/',
         view=auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    # register account
    path(route='register/', view=views.register, name='register'),

    # edit user and profile
    path(route='edit/', view=views.edit, name='edit'),

    path(route='', view=views.dashboard, name='dashboard'),
]
