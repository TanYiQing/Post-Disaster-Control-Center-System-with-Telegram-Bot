from django.urls import path
from . import views

urlpatterns = [
    path('add_profile/', views.add_profile, name="add_profile"),
    path('list_user/', views.list_user, name="list_user"),
    path('edit_profile/<ic>', views.edit_profile, name="edit_profile"),
    path('delete_profile/', views.delete_profile, name="delete_profile"),
]
