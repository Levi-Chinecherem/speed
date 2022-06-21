from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('about/', views.about_view, name='about'),
    path('contact/', views.contact_view, name='contact'),
    path('gallery/', views.gallery_view, name='gallery'),
    path('testimonial/', views.testimonial_view, name='testimony'),
    path('getContact/', views.getContact, name='getContact'),
]