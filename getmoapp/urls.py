
from django.contrib import admin
from django.urls import path
from getmoapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index,name='home'),
    path('starter/', views.starterpage,name='starter'),
]
