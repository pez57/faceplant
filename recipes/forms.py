from django_summernote.widgets import SummernoteWidget
from django import forms
from django.contrib.auth.models import User
from .models import Comment, Recipe
from cloudinary.models import CloudinaryField


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class AddRecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ('author', 'title', 'featured_image', 'category', 'description',
                  'servings', 'ingredients', 'method')

        widgets = {
            # 'author': forms.TextInput(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'ingredients':  SummernoteWidget(),
            'method':  SummernoteWidget(),
        }
