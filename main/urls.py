from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('teashop/', views.teashop, name='teashop'),
    path('pricing/', views.pricing, name='pricing'),
    path('testimonies/', views.testimonies, name='testimonies'),
    path('contact/', views.contact, name='contact'),
    path('services/', views.services, name='services'),
]