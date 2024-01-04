from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('services/', views.services, name='services'),
    path('about/', views.about, name='about'),
    # path('profile/', views.profile, name='profile'),
    # path('calculator/', views.calculator, name='calculator'),
    # Add other paths for your app views
]