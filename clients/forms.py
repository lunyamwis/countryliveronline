from django import forms


class FetchClientsForm(forms.Form):
    start = forms.IntegerField()
    stop = forms.IntegerField()
