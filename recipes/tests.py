from django.test import TestCase
from .models import Recipe


class TestModels(TestCase):

    def test_model_str(self):
        title = Recipe.objects.create(title="Django Testing")
        self.assertEqual(str(title), "Django Testing")
