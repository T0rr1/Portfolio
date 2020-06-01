from django.urls import path
from . import views
from .views import DetailListView, ProjectListView

urlpatterns = [
    path("", ProjectListView.as_view(), name="portafolio-home"),
    path("portafolio/<int:pk>/", DetailListView.as_view(), name="project-detail"),
    path("work/", views.work, name="portafolio-work"),
]
# portafolio/project_list.html
