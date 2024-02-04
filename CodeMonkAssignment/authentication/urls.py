from django.contrib import admin
from django.urls import path
from authentication import views
urlpatterns = [
    path('signup/', views.SignupPage.as_view(), name='signup'),  # DRF Signup endpoint
    path('login/', views.LoginPage.as_view(), name='login'),    # DRF Login endpoint
]