from django import forms
from shirtsapp.models import Decoration

class ShirtForm(forms.ModelForm):
    class Meta:
        model = Decoration
        fields = "__all__"

