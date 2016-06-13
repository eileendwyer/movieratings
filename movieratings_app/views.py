from django.shortcuts import render
from django.http import HttpResponse

from movieratings_app.models import Rater, Movie, Rating
from django.db.models import Count, Avg


def averagerating(request):  # avg rating for top 20
    context = {
    Movie.objects.annotate(average_rating=Avg('movie__rating')).values('title', 'average_rating')\
        .order_by('-average_rating')[:21]
    }
    return render(request, "averagerating.html", context)

def rater_info(request, rater_id):
    context = {
        "rater": Rater.objects.get(id=rater_id),
        "id": rater_id,
        "movies_rated": Movie.objects.annotate(user_rating='rater__rating').values('title', 'rating')
    }
    return render(request, "rater_info.html", context)


def home(request):
    html = "<html><head> <title> Tootie's Movies </title></head></html>" \
           "<body> <h2> Welcome to Tootie's Movies! </h2> </body>"
    return render(request, HttpResponse(html))

# def test_view(request):
#    return render(request, HttpResponse("This is a test!"))


# Create your views here.
