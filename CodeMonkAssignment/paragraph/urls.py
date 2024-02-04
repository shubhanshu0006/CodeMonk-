from django.contrib import admin
from django.urls import path
from paragraph import views
urlpatterns = [
    path('StorePara/', views.StoreParagraphsView.as_view(), name='storepara'),  # DRF Signup endpoint
    path('Search/', views.SearchParagraphsView.as_view(), name='search'),    # DRF Login endpoint
]