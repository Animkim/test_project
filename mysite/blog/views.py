from django.shortcuts import render_to_response
from mysite.blog.models import BlogPost


def archive(request):
    posts = BlogPost.objects.all()
    return render_to_response('archive.html', {'posts': posts})

def post(request, pk):
    context = {'url': BlogPost.get_absolute_url(), 'post': BlogPost.objects.all()}
    return render_to_response('post.html', context)