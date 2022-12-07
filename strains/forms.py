from django import forms

from .models import Strain


class AddStrainForm(forms.ModelForm):
    class Meta:
        model = Strain
        fields = ('name', 'type', 'effect', 'thc', 'aroma', 'description', 'grow_info', 'image')




