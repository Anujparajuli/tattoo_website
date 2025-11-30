from django.shortcuts import render, get_object_or_404, redirect
from .models import Artist, TattooStyle, GalleryImage, Service, Testimonial
from .forms import BookingForm, ContactForm
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Home page
def home(request):
    booking_form = BookingForm()
    contact_form = ContactForm()

    if request.method == 'POST':
        if 'booking_submit' in request.POST:  # Booking form submitted
            booking_form = BookingForm(request.POST, request.FILES)
            if booking_form.is_valid():
                booking_form.save()
                messages.success(request, 'Your booking has been submitted successfully!')
                return redirect('home')
            else:
                messages.error(request, 'There was an error with your booking. Please check the form.')
        
        elif 'contact_submit' in request.POST:  # Contact form submitted
            contact_form = ContactForm(request.POST)
            if contact_form.is_valid():
                contact_form.save()
                messages.success(request, 'Your message has been sent successfully!')
                return redirect('home')

    artists = Artist.objects.filter(show_on_homepage=True)[:8]
    styles = TattooStyle.objects.filter(show_on_homepage=True)[:8]
    gallery_images = GalleryImage.objects.filter(show_on_homepage=True)[:12]
    testimonials = Testimonial.objects.filter(show_on_homepage=True)[:5]

    return render(request, 'index.html', {
        'artists': artists,
        'styles': styles,
        'gallery_images': gallery_images,
        'testimonials': testimonials,
        'form': booking_form,
        'contact_form': contact_form
    })

# Artists page
def artists_page(request):
    artists = Artist.objects.all()
    return render(request, 'artists.html', {'artists': artists})

# Artist detail page
def artist_detail(request, artist_id):
    artist = get_object_or_404(Artist, id=artist_id)
    return render(request, 'artist_detail.html', {'artist': artist})

# Styles page
def styles_view(request):
    styles = TattooStyle.objects.all()
    return render(request, 'styles.html', {'styles': styles})

# Gallery page
def gallery_view(request):
    images = GalleryImage.objects.all()
    return render(request, 'gallery.html', {'images': images})

# Services page
def services_view(request):
    services = Service.objects.all()
    return render(request, 'services.html', {'services': services})

# Pricing page
def pricing_view(request):
    return render(request, 'pricing.html')


# ----------------------------
# AJAX Booking View
# ----------------------------
def booking_view(request):
    """
    This view handles both normal and AJAX submissions.
    On AJAX: returns JSON with success or error messages.
    """
    if request.method == 'POST':
        form = BookingForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Check if AJAX request
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({
                    "success": True,
                    "message": "Your booking was submitted successfully!"
                })
            else:
                messages.success(request, "Your booking was submitted successfully!")
                return redirect('booking')  # or 'home'
        else:
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                # Send back field errors
                errors = {field: [str(e) for e in err] for field, err in form.errors.items()}
                return JsonResponse({"success": False, "errors": errors}, status=400)
    else:
        form = BookingForm()

    return render(request, 'booking.html', {'form': form})


# Contact view (unchanged)
def contact_view(request):
    success = False
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            success = True
            form = ContactForm()  # Reset after save
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form, 'success': success})


# Booking success page (optional)
def booking_success(request):
    return render(request, 'booking_success.html')
