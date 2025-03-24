from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.utils import timezone
from ckeditor.fields import RichTextField
from django.utils.text import slugify

# Create your models here.
class AdminUser(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('author', 'Author'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    def is_admin(self):
        return self.role == 'admin'
    
    def get_absolute_url(self):
        return reverse("USER")
    
class Category(models.Model):
    name = models.CharField(max_length=25)
    slug = models.SlugField(unique=True, blank=True)
    status = models.IntegerField(default=1)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse("CATEGORY")
    
    def __str__(self):
        return self.name
    
class Post(models.Model):
    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to="images/", verbose_name="Post image",)
    status = models.IntegerField(default=1)
    content = RichTextField()
    author = models.ForeignKey(AdminUser, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('POST')
    
class SiteSettings(models.Model):
    name = models.CharField(max_length=30, verbose_name="Blog Name")
    icon = models.ImageField(upload_to="settings/", null=True, blank=True, verbose_name="Blog Icon")
    logo = models.ImageField(upload_to="settings/", null=True, blank=True, verbose_name="Blog Logo")
    about = RichTextField(blank=True, null=True)