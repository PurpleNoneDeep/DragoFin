from django.urls import path
from . import views
from .views import User

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
    path('calendar', views.Calendar, name='calendar'),
    path('dashboard/delete/<int:transaction_id>/', views.delete_transaction, name='delete_transaction'),
    path('dashboard/add/', views.add_transaction, name='add_transaction')
]