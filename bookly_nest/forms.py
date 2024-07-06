
from django import forms
from .models import Genre, Book

class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = ['name']
        labels = {'name': ''}
        
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'genre','publication_year', 'description']
        labels = {
            'title': 'Title', 
            'author': 'Author', 
            'genre': 'Genre'
        }
        widgets = {'description': forms.Textarea(attrs={'cols': 80})}