from django import forms
from .models import Fighter

class FighterForm(forms.ModelForm):
    class Meta:
        model = Fighter
        fields = '__all__'

    widgets = {
        'name': forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your description',
        }),
        'weight_class': forms.NumberInput(attrs={
            'class': 'form-control',
        }),
    }

