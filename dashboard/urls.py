from django.urls import path
from . import views
from .views import booking_view

urlpatterns = [
    path('', views.home, name='home'),
    path('artists/', views.artists_page, name='artists'),
    path('artists/<int:artist_id>/', views.artist_detail, name='artist_detail'),
    path('styles/', views.styles_view, name='styles'),
    path('gallery/', views.gallery_view, name='gallery'),
    path('services/', views.services_view, name='services'),
    path('pricing/', views.pricing_view, name='pricing'),
    path('booking/', booking_view, name='booking'),    path('contact/', views.contact_view, name='contact'),
]


from .views import booking_success

urlpatterns = [
    path('', views.home, name='home'),
    path('artists/', views.artists_page, name='artists'),
    path('artists/<int:artist_id>/', views.artist_detail, name='artist_detail'),
    path('styles/', views.styles_view, name='styles'),
    path('gallery/', views.gallery_view, name='gallery'),
    path('services/', views.services_view, name='services'),
    path('pricing/', views.pricing_view, name='pricing'),
    path('booking/', booking_view, name='booking'),
    path('booking/success/', booking_success, name='booking_success'),  # ✅ Add this
    path('contact/', views.contact_view, name='contact'),
]