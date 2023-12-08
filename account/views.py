from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from .forms import UserRegistrationForm

# Create your views here.

# this function logs user in but it currently not being used since django authentication is being used.


# def user_login(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)

#         if form.is_valid():
#             cd = form.cleaned_data
#             user = authenticate(
#                 request=request,
#                 username=cd['username'],
#                 password=cd['password'],
#             )

#             if user is not None:
#                 if user.is_active:
#                     login(request=request, user=user)
#                     return HttpResponse(content='Authenticated successfully')
#                 else:
#                     return HttpResponse(content='Disabled account')
#             else:
#                 return HttpResponse(content='Invalid login')
#     else:
#         form = LoginForm()

#     return render(request=request, template_name='account/login.html', context={'form': form})


@login_required
def dashboard(request):
    return render(request=request, template_name='account/dashboard.html', context={'section': 'dashboard'})


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)

        if user_form.is_valid():
            # create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # save the User object
            new_user.save()

            return render(request=request, template_name='account/register_done', context={'new_user': new_user})
    else:
        user_form = UserRegistrationForm()

    return render(request=request, template_name='account/register.html', context={'user_form': user_form})
