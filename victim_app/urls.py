from django.urls import path
from . import views

urlpatterns = [
    path('victim/', views.victim, name="victim-application"),
    path('<ic_no>', views.victim_detail, name="victim-detail"),
    path('victim_report/', views.victim_report, name="victim-report"),
]
