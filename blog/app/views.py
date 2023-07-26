from django.shortcuts import render, redirect,HttpResponseRedirect
from .models import BlogPost


recent_post = []
# count_post_view = {}

# counter = 0
# re = {'title':None, 'short':None}

def index(request):

    post = BlogPost.objects.all().order_by('-model_id')
    featured_post = BlogPost.objects.all().order_by('-view_counter')[:8]

    return render(request, 'index.html',{'post':post, 'feature':featured_post})

def addPost(request):
    try:
        author = request.POST.get('author')
        title  = request.POST.get('title')
        short = request.POST.get('short')
        post = request.POST.get('post')
        cat = request.POST.get('cat')
        
        print(author, title, short, post)

        b = BlogPost.objects.create(model_author = author, model_title = title.title(), model_short = short, model_post = post, model_cat = cat.title())
        b.save()

    except Exception as e:
        print(e)

    return render(request, 'addPost.html')


def detailedBlog(request, id):
    
    data = BlogPost.objects.get(model_id = id)
    cat = BlogPost.objects.all().filter(model_cat = data.model_cat)[1:4]
    data.view_counter +=1
    data.save()
    
    featured_post = BlogPost.objects.all().order_by('-view_counter')[:3]
    
    
    
# ----------------------------------------------------------------------------------------------------------
 
    # if id not in recent_post:
    #     recent_post.append(id)

    # if len(recent_post) > 5:
    #     recent_post.pop(0)

    
    # Trying to add recent post but did't work
    # for i in recent_post:
    #     recent = BlogPost.objects.all().filter(model_id = i)
    #     recent_post.append(recent)
    #     # re.update({'title':recent.model_title, 'short':recent.model_short})
    #     for j in recent:
    #         print(j.mo)


    # print(recent_post)
    # --------------------------------------------------------------------------------------------------------------

    return render(request, 'readPost.html', {'id':data, 
                                             'cat':cat,
                                             'featured':featured_post})


def likePost(request, id):
    
    add = BlogPost.objects.get(model_id = id)
 
    count = add.model_like
    count+=1
    add.model_like = count

    add.save()

    return HttpResponseRedirect('/readPost/{}'.format(id))

def byCat(request, cat):

    data = BlogPost.objects.all().values().filter(model_cat = cat)
    
    return render(request, 'byCat.html', {'data':data, 'count':data.count()})