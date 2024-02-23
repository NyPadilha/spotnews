from django.shortcuts import render
from .models import News


# Create your views here.
def home(request):
    news = News.objects.all()

    return render(request, "home.html", {"news": news})


def news_details(request, id):
    news = News.objects.get(pk=id)

    return render(request, "news_details.html", {"news": news})
