from django.urls import path
from .views import HomeView, AboutView, CategoryView, ArticleView

urlpatterns = [
    path("", HomeView.as_view(), name="Index"),
    path("about", AboutView.as_view(), name="About"),
    path("category/<slug:slug>/", CategoryView.as_view(), name="Category_Posts"),
    path("article/<slug:slug>/", ArticleView.as_view(), name="Article_View"),
]