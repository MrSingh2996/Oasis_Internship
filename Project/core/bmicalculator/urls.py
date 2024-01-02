from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('profile/', views.profile, name='profile'),
    # path('calculator/', views.calculator, name='calculator'),
    # Add other paths for your app views
]