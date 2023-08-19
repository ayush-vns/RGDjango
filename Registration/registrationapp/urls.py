from django.urls import path
from . import views

urlpatterns = [

    path("", views.index),
    path("regist",views.regist),
    path("login",views.login)
]