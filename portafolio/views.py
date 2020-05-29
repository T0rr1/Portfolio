from django.shortcuts import render
from .models import Project

# portafolios = [
#     {
#         "title": "Credit Calculator",
#         "description": "This project calculates annuity payment and differentiated payment",
#         "image": "raw.jpg",
#     },
#     {
#         "title": "Tic-Tac-Toe",
#         "description": "A classic tic-tac-toe via command line programmed with python",
#         "image": "zelda.jpg",
#     },
# ]


def home(request):
    return render(
        request, "portafolio/home.html", {"portafolios": Project.objects.all()}
    )


def work(request):
    return render(request, "portafolio/index.html")
