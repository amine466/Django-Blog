from django import forms
from .models import AdminUser, Category, Post, SiteSettings
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class CategoryForm(forms.ModelForm):
    STATUS_CHOICES = [
        ('1', 'Active'),
        ('0', 'Not Active')
    ]
    status = forms.ChoiceField(choices=STATUS_CHOICES)

    class Meta:
        model = Category
        fields = ['name', 'status']

class UserCreateForm(UserCreationForm):
    class Meta:
        model = AdminUser
        fields = ['username', 'email', 'role', 'password1', 'password2']

class UserEditForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(), required=False)
    class Meta:
        model = AdminUser
        fields = ['username', 'email', 'role', 'password']

class PostForm(forms.ModelForm):
    STATUS_CHOICES = [
        ('1', 'Active'),
        ('0', 'Not Active')
    ]
    status = forms.ChoiceField(choices=STATUS_CHOICES)

    class Meta:
        model = Post
        fields = ['title', 'category', 'status', 'image', 'content']
    
class SettingsForm(forms.ModelForm):
    class Meta:
        model = SiteSettings
        fields = ['name', 'icon', 'logo', 'about']