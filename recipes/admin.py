from django.contrib import admin
from .models import Recipe, Comment
from django_summernote.admin import SummernoteModelAdmin
from . import models


@admin.register(Recipe)
class RecipeAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'description', 'servings', 'ingredients']
    list_filter = ('status', 'created_on')
    summernote_fields = ('description', 'ingredients', 'method')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    list_display = ('name', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)


admin.site.register(models.Category)