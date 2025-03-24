from django.urls import path
from .views import Home, category_list, add_category, edit_category, delete_category, user_list, add_user, edit_user, delete_user, post_list, add_post, edit_post, delete_post, view_post, settings_page

urlpatterns = [
    path('', Home.as_view(), name='HOME'),

    path('user/', user_list.as_view(), name="USER"),
    path('user/add/', add_user.as_view(), name="Add_User"),
    path('user/edit/<int:pk>/', edit_user.as_view(), name="Edit_User"),
    path('user/delete/<int:pk>/', delete_user.as_view(), name="Delete_User"),

    path('category/', category_list.as_view(), name="CATEGORY"),
    path('category/add/', add_category.as_view(), name="Add_Category"),
    path('category/edit/<int:pk>/', edit_category.as_view(), name="Edit_Category"),
    path('category/delete/<int:pk>/', delete_category.as_view(), name="Delete_Category"),

    path('post/', post_list.as_view(), name="POST"),
    path('post/add/', add_post.as_view(), name="Add_Post"),
    path('post/edit/<int:pk>/', edit_post.as_view(), name="Edit_Post"),
    path('post/delete/<int:pk>/', delete_post.as_view(), name="Delete_Post"),
    path('post/view/<int:pk>/', view_post.as_view(), name="View_Post"),

    path('settings/', settings_page.as_view(), name="Settings"),
]