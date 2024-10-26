from django.urls import path 
from . import views

urlpatterns = [
    path('', views.public_feed, name="feed"),
    path('register/', views.register, name="register"),
    path('get_app_id/', views.getAppID, name='getAppID'),

    path('add/', views.add_post)
]