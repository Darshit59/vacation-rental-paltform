from django.db import models
from users.models import User
from django.db.models import Avg



# =====================
# PROPERTY
# =====================

class Property(models.Model):

    PROPERTY_TYPES = (
        ('apartment','Apartment'),
        ('house','House'),
        ('villa','Villa'),
        ('cabin','Cabin'),
    )

    host = models.ForeignKey(User, on_delete=models.CASCADE)

    title = models.CharField(max_length=200)

    description = models.TextField()

    location = models.CharField(max_length=200)

    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)

    property_type = models.CharField(max_length=20, choices=PROPERTY_TYPES)

    bedrooms = models.IntegerField()

    bathrooms = models.IntegerField()

    max_guests = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):

        return self.title


    def average_rating(self):

        from reviews.models import Review

        avg = Review.objects.filter(property=self).aggregate(Avg('rating'))

        return avg['rating__avg'] or 0



# =====================
# PROPERTY IMAGE
# =====================

class PropertyImage(models.Model):

    property = models.ForeignKey(Property, on_delete=models.CASCADE)

    image = models.ImageField(upload_to='properties/')


    def __str__(self):

        return self.property.title



# =====================
# EMAIL OTP
# =====================

class EmailOTP(models.Model):

    email = models.EmailField()

    otp = models.CharField(max_length=6)

    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):

        return self.email