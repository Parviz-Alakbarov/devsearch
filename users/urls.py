from django.urls import path, include
from . import views

urlpatterns = [
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerUser, name='register'),

    path('', views.profiles, name='profiles'),
    path('users/', views.profiles, name='profiles'),
    path('profile/<str:pk>', views.userProfile, name='user-profile')
]
