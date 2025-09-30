from django.urls import path
from . import views
from .views import User, user_login

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about),
    path('dashboard', views.dashboard, name='dashboard'),
    path('income', views.income, name='income'),
    path('expences', views.expences, name='expences'),
    path('auth', views.auth, name='auth'),
    path('stistics', views.statistics, name='statistics'),
    path('addtransaction', views.addTransaction, name='addtransaction'),
    path('addcategory', views.addCategory, name='addcategory'),
    path('calendar', views.Calendar, name='calendar')
]