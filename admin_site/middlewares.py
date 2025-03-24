from django.core.exceptions import PermissionDenied
from django.urls import resolve

class AdminOnlyMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        restricted_urls = ['USER', 'Add_User', 'Edit_User', 'Delete_User', 'CATEGORY', 'Add_Category', 'Edit_Category', 'Delete_Category', 'Settings']

        url_name = resolve(request.path_info).url_name

        if url_name in restricted_urls and request.user.is_authenticated:
            if request.user.role != 'admin':
                raise PermissionDenied
            
        return self.get_response(request)