from django.urls import path
from . import views


urlpatterns = [
    path('', views.RecipeList.as_view(), name='home'),
    path('add/', views.AddRecipeView.as_view(), name='add'),
    path('<slug:slug>/edit/', views.EditRecipeView.as_view(), name='recipe_edit'),
    path('<slug:slug>/delete/', views.DeleteRecipeView.as_view(), name='recipe_delete'),
    path('<slug:slug>/', views.RecipeDetail.as_view(), name='recipe_detail'),
    path('like/<slug:slug>', views.RecipeLike.as_view(), name='recipe_like'),
    path('category/<category>/', views.CategoryListView.as_view(), name='category'),
]
