from django.urls import path
from . import views

urlpatterns = [     
    path('teste1/', views.teste1, name='teste'),
]