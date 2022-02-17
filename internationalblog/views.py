from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Post

def index(request):
    # latest_question_list = Post.objects.order_by('-pub_date')[:5]
    posts = Post.objects.select_related('user')[::-1]
    context = {'posts': posts}
    return render(request, 'index.html', context)
def post(request, post_id):
    curr_post = Post.objects.get(pk=post_id)
    context = {
        'post': curr_post,
    }
    # return HttpResponse(template.render(context, request))
    return render(request, 'post.html', context)
