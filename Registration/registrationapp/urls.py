from django.urls import path,include
from . import views
from django.conf.urls.static import static

urlpatterns = [

    path("", views.index),
    path("regist",views.regist),
    path("login",views.login),
    path("img",views.img),
    path("wther",views.weather),
    path("getdata",views.get_planet_data),
    path("fil",views.film),
    path("filmno",views.filmNo),
    path("ayush",views.ayush),
    path("people",views.people),
    path("mcq",views.Mcq),
    path("mcqno",views.MCQno)

]