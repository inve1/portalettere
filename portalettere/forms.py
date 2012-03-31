from django import forms

class SimpleSendForm(forms.Form):
    message = forms.CharField()
