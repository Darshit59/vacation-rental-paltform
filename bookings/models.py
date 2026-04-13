from django.db import models
from users.models import User
from properties.models import Property


class Booking(models.Model):

    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
    )

    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    guest = models.ForeignKey(User, on_delete=models.CASCADE)

    check_in = models.DateField()
    check_out = models.DateField()

    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    booking_status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.property.title} - {self.guest.username}"