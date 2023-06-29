from django.forms import ModelForm, DateInput
from .models import Feeding

class FeedingForm(ModelForm):
  class Meta:
    model = Feeding
    fields = ['date', 'meal']
    widgets = {
      'date': DateInput(attrs={'type': 'date'})
    }