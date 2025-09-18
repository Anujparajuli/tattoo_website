from django.contrib import admin, messages
from .models import Artist, TattooStyle, GalleryImage, Service, Booking
from .models import Testimonial
from django import forms








# Custom form for Artist
class ArtistAdminForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = "__all__"
        widgets = {
            'bio': forms.Textarea(
                attrs={
                    'rows': 4,
                    'cols': 50,
                    'style': 'resize:none;',  # disable resizing
                    'maxlength': '600'        # frontend limit
                }
            ),
        }

# Use single registration
@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    form = ArtistAdminForm
    list_display = ('name', 'instagram', 'tiktok', 'created_at', 'show_on_homepage')
    list_editable = ('show_on_homepage',)
    list_filter = ('show_on_homepage',)













@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'artist', 'description', 'submitted_at']  # use the correct field name




@admin.register(TattooStyle)
class TattooStyleAdmin(admin.ModelAdmin):
    list_display = ('name', 'show_on_homepage')
    # list_editable = ('show_on_homepage',)  # safer to remove
    list_filter = ('show_on_homepage',)

    def save_model(self, request, obj, form, change):
        try:
            super().save_model(request, obj, form, change)
        except ValueError as e:
            self.message_user(request, str(e), level=messages.ERROR)
        except ValidationError as e:
            self.message_user(request, e.messages[0], level=messages.ERROR)





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
