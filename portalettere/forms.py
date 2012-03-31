from django import forms

class SimpleSendForm(forms.Form):
    dest = forms.CharField()
    message = forms.CharField()
