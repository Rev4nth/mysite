from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Post

def post_list(request):
    posts = Post.published.all()
    paginator = Paginator(posts, 3)
    page = request.GET.get('page')
    try:
        posts =  paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
        
    template_path = 'blog/post/list.html'
    context = {
        'posts' : posts,
    }
    return render(request, template_path, context)


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post,
                                   status='published',
                                   publish__year=year,
                                   publish__month=month,
                                   publish__day=day)
    template_path = 'blog/post/detail.html'
    context = {
        'post':post,
    }
    return render(request, template_path, context)
