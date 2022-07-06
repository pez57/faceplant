from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('summernote', include('django_summernote.urls')),
    path('', include('recipes.urls',), name='recipes_urls'),
    path('accounts/', include('allauth.urls')),
]


handler404 = 'recipes.views.not_found'
handler500 = 'recipes.views.error_page'
