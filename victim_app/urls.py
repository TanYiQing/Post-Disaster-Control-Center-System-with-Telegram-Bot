from django.urls import path
from . import views

urlpatterns = [
    path('add_profile/', views.add_profile, name="add_profile"),
    # path('list_user/', views.list_user, name="list_user"),
    # path('edit_profile/', views.edit_profile, name="edit_profile"),

    path('victimdashboard/', views.victim_dashboard, name="victim_dashboard"),
    path('requestassistance/', views.request_assistance, name="victim_request_assistance"),
    path('editassistance/<int:id>', views.edit_assistance, name="victim_edit_assistance"),
    path('viewassistance/', views.view_assistance, name="victim_view_assistance"),
]
