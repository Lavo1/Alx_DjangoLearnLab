from django import forms
from .models import Book
from django.core.exceptions import ValidationError

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'published_date', 'isbn']
        widgets = {
            'published_date': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if "<script>" in title.lower():
            raise ValidationError("No scripts allowed! 🙅🏾‍♀️")
        return title

    def clean_isbn(self):
        isbn = self.cleaned_data.get('isbn')
        if not isbn.isdigit():
            raise ValidationError("ISBN must only contain numbers.")
        return isbn
        
class ExampleForm(forms.Form):
    example_field = forms.CharField(label='Example Field', max_length=100)