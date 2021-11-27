from django.urls import path

from . import views

urlpatterns = [
    path("create/", views.request_assistance, name='request-assistance'),

]