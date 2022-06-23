
from django.forms import ModelForm 
from .models import command

class commandForm(ModelForm):
    class Meta:
        model=command
        fields='__all__'