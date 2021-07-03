from django import forms
from django.forms.fields import CharField, ChoiceField
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import Publisher, Review, Book

CHOICES = (("title", "Title"), ("contributor", "Contributor"))

class SearchForm(forms.Form):
    search = CharField(required=False, min_length=3)
    search_in = ChoiceField(required=False, choices=CHOICES)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "get"
        self.helper.add_input(Submit("", "Search"))

class PublisherForm(forms.ModelForm):
    class Meta:
        model = Publisher
        fields = "__all__"

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        exclude = ["date_editied", "book"]
        rating = forms.IntegerField(min_value=0, max_value=5)

class BookMediaForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["cover", "sample"]