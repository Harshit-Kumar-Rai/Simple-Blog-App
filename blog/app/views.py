from django.shortcuts import render, redirect,HttpResponseRedirect
from .models import BlogPost
# Create your views here.
def index(request):

    post = BlogPost.objects.all()

    return render(request, 'index.html',{'post':post})

def addPost(request):
    try:
        author = request.POST.get('author')
        title  = request.POST.get('title')
        short = request.POST.get('short')
        post = request.POST.get('post')

        print(author, title, short, post)

        b = BlogPost.objects.create(model_author = author, model_title = title, model_short = short, model_post = post)
        b.save()

    except Exception as e:
        print(e)

    return render(request, 'addPost.html')

def detailedBlog(request, id):

    data = BlogPost.objects.get(model_id = id)

    return render(request, 'readPost.html', {'id':data})


def likePost(request, id):
    
    add = BlogPost.objects.get(model_id = id)
 
    count = add.model_like
    count+=1
    add.model_like = count

    add.save()

    return HttpResponseRedirect('/readPost/{}'.format(id))