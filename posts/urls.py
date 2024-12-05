from django.contrib import admin
from django.urls import path
from posts import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/', views.posts_list),
    path('posts/<int:id>', views.post_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)