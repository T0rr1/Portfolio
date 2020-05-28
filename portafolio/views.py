from django.shortcuts import render

portafolios = [
    {
        "title": "Credit Calculator",
        "description": "This project calculates annuity payment and differentiated payment",
        "image": "raw.jpg",
    },
    {
        "title": "Tic-Tac-Toe",
        "description": "A classic tic-tac-toe via command line programmed with python",
        "image": "zelda.jpg",
    },
    {
        "title": "Credit Calculator",
        "description": "This project calculates annuity payment and differentiated payment",
        "image": "raw.jpg",
    },
]


def home(request):
    return render(request, "portafolio/home.html", {"portafolios": portafolios})


def cv(request):
    return render(request, "portafolio/index.html")
