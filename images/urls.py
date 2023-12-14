from django.urls import path

from . import views

app_name = 'images'

urlpatterns = [
    path(route='create/', view=views.image_create, name='create'),
]
