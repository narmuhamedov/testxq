from django.urls import path
from . import views

urlpatterns = [
  path('', views.FirstLessonView.as_view(), name='main_page'),
]