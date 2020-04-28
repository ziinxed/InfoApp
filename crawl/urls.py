from django.urls import path
from crawl import views

urlpatterns = [
    path('crawl/', views.link_list),
    path('crawl/<int:pk>/', views.link_detail),
]