from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from . models import Blog, Category


# Create your views here.
def posts_by_category(request, category_id):
    #print(category_id)
    
    #fetch the post thaat belong to category with id which is Category_id
    posts = Blog.objects.filter(status='published', category_id=category_id)
    #use try/except when we want to do some cutom action if the categoru does not exists
    # try:
    #     category = Category.objects.get(pk=category_id)
    # except:
    #     return redirect('home')

    #use get_object_or_404 when you want ro show 404 erroe page if the category does not exist
    category = get_object_or_404(Category, pk=category_id)

    context = {
        'posts': posts,
        'category': category
    }
    return render(request, 'posts_by_category.html', context)