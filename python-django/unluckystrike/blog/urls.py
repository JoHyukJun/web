from django.urls import path
from django.urls import include
from . import views


urlpatterns = [
    path('', views.blog_index, name="blog_index"),
    path('<int:pk>/<title>', views.blog_detail, name="blog_detail"),
    path('<category>/', views.blog_category, name="blog_category"),
]