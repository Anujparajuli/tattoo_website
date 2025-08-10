from django.contrib import admin
from .models import Artist, TattooStyle, GalleryImage, Service, Booking
from .models import Testimonial

@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ('name', 'instagram', 'tiktok', 'created_at', 'show_on_homepage')
    list_editable = ('show_on_homepage',)
    list_filter = ('show_on_homepage',)


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'artist', 'description', 'submitted_at']  # use the correct field name


@admin.register(TattooStyle)
class TattooStyleAdmin(admin.ModelAdmin):
    list_display = ('name', 'show_on_homepage')
    list_editable = ('show_on_homepage',)
    list_filter = ('show_on_homepage',)


@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ('caption', 'category', 'show_on_homepage')
    list_editable = ('show_on_homepage',)
    list_filter = ('category', 'show_on_homepage')


admin.site.register(Service)




@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('author', 'stars', 'show_on_homepage')
    list_editable = ('show_on_homepage',)
    list_filter = ('show_on_homepage',)
    

from .models import ContactMessage



@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at')
    search_fields = ('name', 'email', 'subject', 'message')
