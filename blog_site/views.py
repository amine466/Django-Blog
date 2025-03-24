from django.shortcuts import render
from admin_site.models import Category, Post, SiteSettings
from django.views.generic import TemplateView, ListView, DetailView
from django.shortcuts import get_object_or_404

# Create your views here.
class HomeView(ListView):
    model = Post
    template_name = "home.html"
    context_object_name = "posts"
    paginate_by = 6  

    def get_queryset(self):
        return Post.objects.filter(status=1).order_by("-created_at")[1:]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["latest_post"] = Post.objects.filter(status=1).order_by("-created_at").first()
        context["categories"] = Category.objects.all()
        context["settings"] = get_object_or_404(SiteSettings, id=1)
        return context
    
class AboutView(TemplateView):
    template_name = "pages/about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        context["settings"] = get_object_or_404(SiteSettings, id=1)
        return context

class CategoryView(ListView):
    model = Post
    template_name = "pages/category.html"
    context_object_name = "posts"
    paginate_by = 6

    def get_queryset(self):
        category = get_object_or_404(Category, slug=self.kwargs["slug"])
        return Post.objects.filter(category=category, status=1)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cat"] = get_object_or_404(Category, slug=self.kwargs["slug"])
        context["categories"] = Category.objects.all()
        context["settings"] = get_object_or_404(SiteSettings, id=1)
        return context
    
class ArticleView(DetailView):
    model = Post
    template_name = "pages/article.html"
    context_object_name = "post"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        context["settings"] = get_object_or_404(SiteSettings, id=1)
        return context