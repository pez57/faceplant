from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from autoslug import AutoSlugField


STATUS = ((0, "Draft"), (1, "Published"))


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    title = models.CharField(max_length=200, unique=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=False)
    slug = AutoSlugField(populate_from='title', always_update=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name="recipe_posts")
    updated_on = models.DateTimeField(auto_now=True)
    description = models.TextField()
    servings = models.IntegerField(default=1)
    featured_image = CloudinaryField('image', default='placeholder')
    ingredients = models.TextField(default='Please Use bulletpoints for each ingredient')
    method = models.TextField(default=' Please Use numbered list for each method step')
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=1)
    likes = models.ManyToManyField(User, related_name='recipe_likes', blank=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()


class Comment(models.Model):
    """
    Comment model code adapted from Code Institue 
    Walkthrough Project
    """
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE,
                               related_name="comments")
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f"Comment {self.body} by {self.name}"
