from django import forms

class NameForm(forms.Form):
    phone = forms.CharField(max_length=13)
    password = forms.CharField(max_length=8)