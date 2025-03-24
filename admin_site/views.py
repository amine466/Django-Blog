from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import AdminUser, Category, Post, SiteSettings
from .forms import CategoryForm, PostForm, UserCreateForm, UserEditForm, SettingsForm
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import update_session_auth_hash

# Create your views here.
class Home(LoginRequiredMixin, TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'], context['categorie'], context['post'] = (
            AdminUser.objects.count(),
            Category.objects.count(),
            Post.objects.count()
        )
        context['posts'] = Post.objects.order_by('-created_at')[:5]
        return context

class user_list(LoginRequiredMixin, ListView):
    model = AdminUser
    template_name = 'pages/user/user.html'
    context_object_name = 'users'
    paginate_by = 5

class add_user(LoginRequiredMixin, CreateView):
    model = AdminUser
    template_name = 'pages/user/user_add.html'
    form_class = UserCreateForm

    def form_valid(self, form):
        messages.success(self.request, "User created successfully")
        return super().form_valid(form)

class edit_user(LoginRequiredMixin, UpdateView):
    model = AdminUser
    template_name = 'pages/user/user_edit.html'
    form_class = UserEditForm

    def form_valid(self, form):
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')

        if password:
            user.set_password(password)
        user.save()
        update_session_auth_hash(self.request, user)
        messages.success(self.request, 'User updated successfully')
        return super().form_valid(form)
    
class delete_user(LoginRequiredMixin, DeleteView):
    model = AdminUser
    success_url = reverse_lazy('USER')

    def post(self, request, *args, **kwargs):
        self.get_object().delete()
        messages.success(self.request, "User Deleted successfully")
        return redirect(self.success_url)

class category_list(LoginRequiredMixin, ListView):
    model = Category
    template_name = 'pages/category/category.html'
    context_object_name = 'categories'
    paginate_by = 5

class add_category(LoginRequiredMixin, CreateView):
    model = Category
    template_name = 'pages/category/category_add.html'
    form_class = CategoryForm

    def form_valid(self, form):
        messages.success(self.request, "Category created successfully")
        return super().form_valid(form)
    
class edit_category(LoginRequiredMixin, UpdateView):
    model = Category
    template_name = 'pages/category/category_edit.html'
    form_class = CategoryForm

    def form_valid(self, form):
        messages.success(self.request, "Category updated successfully")
        return super().form_valid(form)

class delete_category(LoginRequiredMixin, DeleteView):
    model = Category
    success_url = reverse_lazy('CATEGORY')
    def post(self, request, *args, **kwargs):
        self.get_object().delete()
        messages.success(self.request, "Category Deleted successfully")
        return redirect(self.success_url)
    
class post_list(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'pages/post/post.html'
    context_object_name = 'posts'
    paginate_by = 5

class add_post(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'pages/post/post_add.html'
    form_class = PostForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, "Post created successfully")
        return super().form_valid(form)
    
class edit_post(LoginRequiredMixin, UpdateView):
    model = Post
    template_name = 'pages/post/post_edit.html'
    form_class = PostForm

    def form_valid(self, form):
        messages.success(self.request, "Post updated successfully")
        return super().form_valid(form)
    
class delete_post(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('POST')

    def post(self, request, *args, **kwargs):
        self.get_object().delete()
        messages.success(self.request, "Post deleted successfully")
        return redirect(self.success_url)
    
class view_post(LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'pages/post/post_view.html'
    context_object_name = 'post'
    paginate_by = 5

class settings_page(LoginRequiredMixin, UpdateView):
    model = SiteSettings
    template_name = 'pages/settings.html'
    form_class = SettingsForm
    success_url = reverse_lazy('Settings')

    def get_object(self, queryset = None):
        return SiteSettings.objects.get_or_create(pk=1)[0]