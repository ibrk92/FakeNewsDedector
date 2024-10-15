from django import forms
from .models import NewsArticle

class NewsArticleForm(forms.ModelForm):
    class Meta:
        model = NewsArticle
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={'class': 'form-control', 'rows': 5})  # Burada widget özelliklerini ayarlıyoruz
        }

