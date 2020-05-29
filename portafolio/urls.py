from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="portafolio-home"),
    path("work/", views.work, name="portafolio-work"),
]
