from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name="dashboard"),
    path('listvictim/', views.list_victim, name="list_victim"),
]
