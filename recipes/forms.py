from django_summernote.widgets import SummernoteWidget
from django import forms
from .models import Comment, Recipe


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class AddRecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ('title', 'featured_image', 'category', 'description',
                  'servings', 'ingredients', 'method')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'ingredients':  SummernoteWidget(),
            'method':  SummernoteWidget(),
        }
