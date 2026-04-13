from django import forms
from .models import Property

class PropertyForm(forms.ModelForm):

    class Meta:
        model = Property

        fields = [
            'title',
            'description',
            'location',
            'price_per_night',
            'property_type',
            'bedrooms',
            'bathrooms',
            'max_guests'
        ]