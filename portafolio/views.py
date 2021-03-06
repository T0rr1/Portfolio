from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Project

# {"portafolios": Project.objects.all()}


def home(request):
    return render(request, "portafolio/landing.html")


class ProjectListView(ListView):
    model = Project
    template_name = "portafolio/home.html"
    context_object_name = "portafolios"
    ordering = "-date_posted"


class DetailListView(DetailView):
    model = Project


def cv(request):
    return render(request, "portafolio/index.html")
