from django.urls import path
from . import views

urlpatterns = [
    path('fighters/', views.fighter_list, name='fighter_list'),
    path('fighters/create/', views.fighter_create, name='fighter_create'),
    path('fighters/<int:pk>/edit/', views.fighter_update, name='fighter_update'),
    path('fighters/<int:pk>/delete/', views.fighter_delete, name='fighter_delete'),
    path('logout/', views.logout_view, name='logout'),
    path('fighter/update/<int:pk>/', views.fighter_update_form, name='fighter_update_form')
]