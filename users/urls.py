from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.profiles, name='profiles'),
    path('users/', views.profiles, name='profiles'),
    path('profile/<str:pk>', views.userProfile, name='user-profile')
]
