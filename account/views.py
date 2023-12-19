from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages

from .forms import UserRegistrationForm, UserEditForm, ProfileEditForm
from .models import Profile

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
            # create the user profile
            Profile.objects.create(user=new_user)
            return render(request=request, template_name='account/register_done.html', context={'new_user': new_user})
    else:
        user_form = UserRegistrationForm()

    return render(request=request, template_name='account/register.html', context={'user_form': user_form})


@login_required
def edit(request):
    if request.method == 'POST':
        # from google bard
        # you can use both instance and data together to initialize a form.
        # in this case, the data parameter will take precedence over the instance parameter for any conflicting values
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(
            instance=request.user.profile, data=request.POST, files=request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(
                request=request, message='Profile updated successfully')
        else:
            messages.error(request=request,
                           message='Error updating your profile')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)

    return render(request=request, template_name='account/edit.html', context={'user_form': user_form, 'profile_form': profile_form})


@login_required
def user_list(request):
    users = User.objects.filter(is_active=True)

    return render(request=request, template_name='account/user/list.html', context={'section': 'people', 'users': users})


@login_required
def user_detail(request, username):
    user = get_object_or_404(klass=User, username=username, is_active=True)

    return render(request=request, template_name='account/user/detail.html', context={'section': 'people', 'user': user})
