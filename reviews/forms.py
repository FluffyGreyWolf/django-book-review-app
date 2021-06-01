from django import forms
from django.forms.fields import CharField, ChoiceField

CHOICES = (("title", "Title"), ("contributor", "Contributor"))

class SearchForm(forms.Form):
    search = CharField(required=False, min_length=3)
    search_in = ChoiceField(required=False, choices=CHOICES)