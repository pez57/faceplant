from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from .forms import CommentForm, AddRecipeForm
from .models import Recipe, Category


class DeleteRecipeView(SuccessMessageMixin, DeleteView):

    model = Recipe
    template_name = 'confirm_delete.html'
    success_message = "Recipe has been deleted"
    success_url = reverse_lazy('view_all')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(DeleteRecipeView, self).delete(request, *args, **kwargs)

    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(
            author=self.request.user
        )


class EditRecipeView(SuccessMessageMixin, LoginRequiredMixin,  UpdateView):

    login_url = '/accounts/login/'
    redirect_field_name = 'account_login'

    model = Recipe
    form_class = AddRecipeForm
    template_name = 'add.html'
    success_message = "Recipe was updated successfully"

    def get_success_url(self):
        return reverse_lazy('recipe_detail', kwargs={'slug': self.object.slug})

    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(
            author=self.request.user
        )
 


class AddRecipeView(SuccessMessageMixin, LoginRequiredMixin, CreateView):

    model = Recipe
    form_class = AddRecipeForm
    template_name = 'add.html'

    login_url = '/accounts/login/'
    redirect_field_name = 'account_login'
    success_message = "Recipe was added successfully"

    def get_success_url(self):
        return reverse_lazy('recipe_detail', kwargs={'slug': self.object.slug})

    def get_initial(self, *args, **kwargs):
        initial = super().get_initial(**kwargs)
        initial['author'] = self.request.user
        return initial



class RecipeList(generic.ListView):
    model = Recipe
    queryset = Recipe.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"
    paginate_by = 6


class RecipeDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Recipe.objects.filter(status=1)
        recipe = get_object_or_404(queryset, slug=slug)
        comments = recipe.comments.filter(approved=True).order_by('created_on')
        liked = False
        if recipe.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "recipe_detail.html",
            {
                "recipe": recipe,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )


    def post(self, request, slug, *args, **kwargs):
        queryset = Recipe.objects.filter(status=1)
        recipe = get_object_or_404(queryset, slug=slug)
        comments = recipe.comments.filter(approved=True).order_by('created_on')
        liked = recipe.likes.filter(id=self.request.user.id).exists()

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.recipe = recipe
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "recipe_detail.html",
            {
                "recipe": recipe,
                "comments": comments,
                "commented": True,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )


class RecipeLike(View):

    def post(self, request, slug, *args, **kwargs):
        recipe = get_object_or_404(Recipe, slug=slug)

        if recipe.likes.filter(id=request.user.id).exists():
            recipe.likes.remove(request.user)
        else:
            recipe.likes.add(request.user)

        return HttpResponseRedirect(reverse('recipe_detail', args=[slug]))


class AllRecipes(generic.ListView):
    model = Recipe
    queryset = Recipe.objects.filter(status=1).order_by("-created_on")
    template_name = "view_all.html"
    paginate_by = 6


class CategoryListView(ListView):
    template_name = 'category.html'
    context_object_name = 'catlist'
    #Adds category name to kwargs
    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs)
        context['category'] = self.kwargs['category']
        return context

    def get_queryset(self):
        content = {
            'cat': self.kwargs['category'],
            'recipes': Recipe.objects.filter(category__name=self.kwargs
            ['category']).filter(status=1)
        }
        return content



def category_list(request):
    category_list = Category.objects.exclude(name='default')
    context = {
        'category_list': category_list,
    }
    return context


# Custom error pages
def not_found(request, exception):
    return render(request, '404.html')


def error_page(request, exception=None):
    return render(request, '500.html')