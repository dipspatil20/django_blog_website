from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from . models import Blog, Category, Comment
from django.db.models import Q


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

def blogs(request, slug):
    single_blog = get_object_or_404(Blog, slug=slug, status='published')
    if request.method == 'POST':
        comment = Comment()
        comment.user = request.user
        comment.blog = single_blog
        comment.comment = request.POST['comment']
        comment.save()
        return HttpResponseRedirect(request.path_info)


    # Comments
    comments = Comment.objects.filter(blog=single_blog)
    comment_count = comments.count()

    context = {
        'single_blog':single_blog,
        'comments': comments,
        'comment_count': comment_count,
    }
    return render(request, 'blogs.html', context)


def search(request):
    keyword = request.GET.get('keyword')
    
    blogs = Blog.objects.filter(Q(title__icontains=keyword) | Q(short_description__icontains=keyword) | Q(blog_body__icontains=keyword), status='published')
    context = {
        'blogs': blogs,
        'keyword': keyword,
    }
    return render(request, 'search.html', context)