from django.forms import ModelForm
from . models import Bookinfo

class Bookform(ModelForm):
    class Meta:
        model=Bookinfo
        fields='__all__'
