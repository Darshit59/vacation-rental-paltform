from django.db import models
from users.models import User
from properties.models import Property


class Review(models.Model):

    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    guest = models.ForeignKey(User, on_delete=models.CASCADE)

    rating = models.IntegerField()
    comment = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.property)