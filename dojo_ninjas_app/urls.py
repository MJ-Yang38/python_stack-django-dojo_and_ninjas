from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('new_dojo',views.new_dojo),
    path('new_ninja',views.new_ninja),
]