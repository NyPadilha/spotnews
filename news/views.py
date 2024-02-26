from django.shortcuts import render, redirect
from rest_framework.viewsets import ModelViewSet
from .models import News, Category
from .forms import CreateCategoryForm, CreateNewsForm
from .serializers import CategorySerializer


# Create your views here.
def home(request):
    news = News.objects.all()

    return render(request, "home.html", {"news": news})


def news_details(request, id):
    news = News.objects.get(pk=id)

    return render(request, "news_details.html", {"news": news})


def categories_form(request):
    form = CreateCategoryForm()

    if request.method == "POST":
        form = CreateCategoryForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("home-page")

    return render(request, "categories_form.html", {"form": form})


def news_form(request):
    form = CreateNewsForm()

    if request.method == "POST":
        form = CreateNewsForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect("home-page")

    return render(request, "news_form.html", {"form": form})


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
