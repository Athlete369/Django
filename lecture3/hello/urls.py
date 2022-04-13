from django import views
from django.urls import path
from . import views
urlpatterns =[
    path("", views.index, name="index"),
    path("/trija",views.trija,name="trija"),
    path("/<str:name>",views.greet,name="greet")
]