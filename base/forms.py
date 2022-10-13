from django.forms import ModelForm
from .models import NFTname


class NFtnameForm(ModelForm):
    class Meta:
        model=NFTname
        fields='__all__'