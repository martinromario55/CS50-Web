from .models import *
from django import forms
from django.core.validators import FileExtensionValidator


class CreateListingForm(forms.ModelForm):
    title = forms.CharField(label="Title", max_length=64, min_length=2)
    description = forms.CharField(label="Description", min_length=5, max_length=255, widget=forms.Textarea)
    bid_amount = forms.IntegerField(min_value=1)
    image = forms.ImageField(validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])], required=False)
    # category = forms.CharField(choices=Categories.objects.all(), widget=forms.Select(attrs={'class': 'custom-select'}))
    category_choices = [(None, '------')] + [(category.id, category.title) for category in Categories.objects.all()]
    category = forms.ChoiceField(choices=category_choices, required=False)
    class Meta:
        model = Auction_listings
        fields = ['title', 'description', 'bid_amount', 'image', 'category']