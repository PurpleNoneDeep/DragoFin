from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about),
    path('dashboard', views.dashboard, name='dashboard'),
    path('income', views.income, name='income'),
    path('expences', views.expences, name='expences')
]