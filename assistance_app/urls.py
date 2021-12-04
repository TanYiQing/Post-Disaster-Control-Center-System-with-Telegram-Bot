from django.urls import path
from . import views

urlpatterns = [
    path("create/", views.request_assistance, name='request-assistance'),
    path('requestassistance/', views.add, name="add"),
    path("applicationrecord/", views.list_assistance_type, name='list_assistance_type'),
    path("edit/<id>", views.edit_assistance_type, name='edit_assistance_type'),
]