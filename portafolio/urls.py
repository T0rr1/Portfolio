from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="portafolio-home"),
    path("cv/", views.cv, name="portafolio-cv"),
]
