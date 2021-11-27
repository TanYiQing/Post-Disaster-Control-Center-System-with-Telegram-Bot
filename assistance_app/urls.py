from django.urls import path
from assistance_app import views


urlpatterns = [
    path('add/', views.add, name="add"),
]