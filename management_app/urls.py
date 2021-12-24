from django.urls import path
from . import views

urlpatterns = [
    path('listvictim/', views.list_victim, name="list_victim"),

]