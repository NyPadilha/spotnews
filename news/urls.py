from django.urls import path, include
from .views import (
    home,
    news_details,
    categories_form,
    news_form,
    CategoryViewSet,
)
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r"categories", CategoryViewSet)


urlpatterns = [
    path("", home, name="home-page"),
    path("news/<int:id>", news_details, name="news-details-page"),
    path("categories", categories_form, name="categories-form"),
    path("news", news_form, name="news-form"),
    path("api/", include(router.urls)),
]
