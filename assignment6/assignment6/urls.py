from django.urls import path
from . import views

app_name = 'bitwise'

urlpatterns = [
    path('', views.index, name='index'),
    path('history/', views.history, name='history'),
]