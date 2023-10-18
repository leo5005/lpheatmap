from django import forms
from .models import Url_Form

class User_Form(forms.ModelForm):
    class Meta:
        model=Url_Form
        fields=('web_site',)
        
        error_messages = {
            'comment': {
                'required': "URLを入力してください",
            },
        }
                  