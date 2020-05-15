from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from crawl import views

urlpatterns = [
    path('crawl/', views.link_list),
    path('crawl/<int:pk>', views.link_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)
