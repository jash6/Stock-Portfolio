from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/',views.about, name='about'),
    path('dashboard/',views.dashboard, name='dashboard'),
    path('delete/<stock_id>',views.delete,name='delete'),
    path('deletestock/',views.deletestock, name='deletestock'),
]
