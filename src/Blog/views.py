from django.shortcuts import render
import random


# Create your views here.
def index(request):
    return render(request, "Blog/index.html")


def def_mate(request, mate):
    rand = random.randint(0, 50)

    if mate == "gold":
        color = 'yellow'
    elif mate == "marble":
        color = 'brown'
    elif mate == "silver":
        color = 'gray'

    if mate in [
        "gold",
        "marble",
        "silver",
    ]:
        up = rand + random.randint(0, 100)
        down = 100 - up
        return render(request, "Blog/mate.html", context={"mate": mate, "up": up, "down": down, 'color': color, })
    return render(request, "Blog/not_found.html")
