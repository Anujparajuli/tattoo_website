from django.db import models

# Create your models here.

from django.core.validators import MaxLengthValidator

from django.core.exceptions import ValidationError


class Artist(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField(validators=[MaxLengthValidator(600)])  # limit bio to 300 chars
    image = models.ImageField(upload_to='artists/')
    instagram = models.URLField(blank=True, null=True)
    tiktok = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    show_on_homepage = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if self.show_on_homepage and Artist.objects.filter(show_on_homepage=True).exclude(pk=self.pk).count() >= 6:
            raise ValueError("You can only have 6 artists on the homepage.")
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name



class TattooStyle(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='style_images/')
    show_on_homepage = models.BooleanField(default=False)

    def clean(self):
        # Limit description to 50 words
        word_count = len(self.description.split())
        if word_count > 50:
            raise ValidationError("Description cannot exceed 50 words.")

    def save(self, *args, **kwargs):
        self.clean()  # enforce validation
        # Limit number of styles on homepage
        if self.show_on_homepage and TattooStyle.objects.filter(show_on_homepage=True).exclude(pk=self.pk).count() >= 6:
            raise ValueError("You can only have 6 styles on the homepage.")
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class GalleryImage(models.Model):
    CATEGORY_CHOICES = [
        ('blackgrey', 'Black & Grey'),
        ('color', 'Color'),
        ('lettering', 'Lettering'),
        ('sleeve', 'Sleeve'),
        ('small', 'Small Tattoos'),
    ]
    image = models.ImageField(upload_to='gallery/')
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    caption = models.CharField(max_length=100, blank=True)
    show_on_homepage = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if self.show_on_homepage and GalleryImage.objects.filter(show_on_homepage=True).exclude(pk=self.pk).count() >= 12:
            raise ValueError("You can only have 12 gallery images on the homepage.")
        super().save(*args, **kwargs)

    def __str__(self):
        return self.caption or f"{self.category} Image"

class Service(models.Model):
    ICON_CHOICES = [
        ('fas fa-paint-brush', 'Paint Brush'),
        ('fas fa-shield-alt', 'Shield'),
        ('fas fa-hand-sparkles', 'Hand Sparkles'),
        ('fas fa-brush', 'Brush'),
        ('fas fa-bolt', 'Bolt'),
        ('fas fa-spray-can', 'Spray Can'),
    ]

    title = models.CharField(max_length=100)
    description = models.TextField()
    icon_class = models.CharField(max_length=50, choices=ICON_CHOICES)

    def __str__(self):
        return self.title



class Booking(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    artist = models.CharField(max_length=100, blank=True)
    placement = models.CharField(max_length=255, blank=True)
    description = models.TextField()
    reference = models.ImageField(upload_to='booking_references/', blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"

from django.core.validators import MinValueValidator, MaxValueValidator

class Testimonial(models.Model):
    author = models.CharField(max_length=100)
    text = models.TextField()
    stars = models.PositiveSmallIntegerField(
        default=5,
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    created_at = models.DateTimeField(auto_now_add=True)
    show_on_homepage = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if self.show_on_homepage and Testimonial.objects.filter(show_on_homepage=True).exclude(pk=self.pk).count() >= 5:
            raise ValueError("You can only have 5 testimonials on the homepage.")
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.author} – {self.stars}★"

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"


