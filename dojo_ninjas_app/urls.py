from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('dojo_form', views.dojo_form),
    path('create_dojo', views.create_dojo),
    path('create_ninja', views.create_ninja),
    path('ninja_form', views.ninja_form),
]