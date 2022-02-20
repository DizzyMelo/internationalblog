from datetime import datetime
from django.shortcuts import render

from .forms import AddPostForm

from .models import Post, User

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

def new_post(request):
    return render(request, 'new_post.html')


def add_post(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST)
        if form.is_valid():
            post_title = form.cleaned_data['post_title']
            post_description = form.cleaned_data['post_description']
            post_message = form.cleaned_data['post_message']
            Post.objects.create(user = User.objects.get(pk=1), 
                                post_title = post_title, 
                                post_description = post_description, 
                                post_message = post_message, 
                                post_date = datetime.now(),
                                status = True)
            return render(request, 'thanks.html')
        else:
            form = AddPostForm()
    
    return render(request, 'index.html')

    
    
def thanks(request):
    return render(request, 'thanks.html')
