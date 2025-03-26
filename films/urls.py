from django.urls import path
from . import views

urlpatterns = [
  path('film_list/', views.film_list, name='films'),
  path('film_list/<int:id>/', views.film_detail, name='film_detail'),
]