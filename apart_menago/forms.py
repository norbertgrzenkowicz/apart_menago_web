from django import forms


class NameForm(forms.Form):
    dupa = forms.CharField(label="Dupa?", max_length=100)
