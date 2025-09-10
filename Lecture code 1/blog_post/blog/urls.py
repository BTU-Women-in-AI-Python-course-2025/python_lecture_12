from django.urls import path
from blog.views import home_view, blog_list, blog_detail, not_found

urlpatterns = [
    path('home/', home_view, name='home'),
    path('blogs/', blog_list, name='blog_list'),
    path("blogs/<int:post_id>/", blog_detail, name="blog_detail"),
    path('not_fount/', not_found, name='not_found')
]
