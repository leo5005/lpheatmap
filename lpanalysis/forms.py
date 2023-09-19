from django import forms
from .models import Url_Form

class User_Form(forms.ModelForm):
    class Meta:
        model=Url_Form
        fields=('user','web_site',)
                  