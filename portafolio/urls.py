from django.urls import path
from . import views
from .views import DetailListView, ProjectListView

urlpatterns = [
    path("", views.home, name="portafolio-home"),
    path("portfolio/<int:pk>/", DetailListView.as_view(), name="project-detail"),
    path("portfolio/", ProjectListView.as_view(), name="portafolio-work"),
    path("cv/", views.cv, name="portafolio-cv"),
]
# portafolio/project_list.html
