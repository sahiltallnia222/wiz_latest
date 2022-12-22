from django.shortcuts import render,redirect
from .models import Post,Tag,HeaderPosts
from .models import Comment
from django.http import JsonResponse,HttpResponse
from rest_framework.decorators import api_view
from .serializers import PostSerializer,HeaderPostSerializer,CommentSerializer
from rest_framework.response import Response
from django.db.models import Count
from django.contrib.auth.models import AnonymousUser
from django.contrib import auth,messages

@api_view(['GET'])
def load_cat_posts(request,category):
    if(request.method=='GET'):
        page_number=request.GET.get('page')
        tag_value=request.GET.get('tag')
        if tag_value:
            try:
                tag=Tag.objects.get(tag__exact=tag_value)
                load_posts=Post.objects.filter(category=category ,tag=tag)[8*(int(page_number)-1):8*(int(page_number)-1)+8]
                total_posts=Post.objects.filter(category=category ,tag=tag).count()
                serializer=PostSerializer(load_posts,many=True)
                return Response({'data':serializer.data,'total_posts':total_posts})
            except:
                total_posts=0
                return Response({'data':[],'total_posts':total_posts})
        else:
            load_posts=Post.objects.filter(category=category)[8*(int(page_number)-1):8*(int(page_number)-1)+8]
            total_posts=Post.objects.filter(category=category).count()
            serializer=PostSerializer(load_posts,many=True)
            return Response({'data':serializer.data,'total_posts':total_posts})




def post_details(request,slug):
    # try:
        post=Post.objects.get(slug=slug)
        tags=Tag.objects.all()
        total_comments=len(post.post_comment.all())
        total_likes=len(post.likes.all())
        if(request.user!=AnonymousUser() and post.likes.contains(request.user)):
            like_btn_class='fa-solid'
        else:
            like_btn_class='fa-regular'
            
        rec_posts_slug=post.rec_posts.split('-')  
        if Post.objects.filter(id=rec_posts_slug[0]).exists():
                post_1=Post.objects.get(id=rec_posts_slug[0])
        else:
            post_1=Post.objects.get(id=1)
            
        if Post.objects.filter(id=rec_posts_slug[1]).exists():
                post_2=Post.objects.get(id=rec_posts_slug[1])
        else:
             post_2=Post.objects.get(id=2)
        
        if Post.objects.filter(id=rec_posts_slug[2]).exists():
                post_3=Post.objects.get(id=rec_posts_slug[2])
        else:
            post_3=Post.objects.get(id=3)
        if request.user.is_authenticated:
            user=1
        else:
            user=0
        context={
            'post':post,
            'slug':slug,
            'total_likes':total_likes,
            'like_btn_class':like_btn_class,
            'tags':tags,
            'total_comments':total_comments,
            'post_1':post_1,
            'post_2':post_2,
            'post_3':post_3,
            'user':user
        }
        return render(request,'posts/postview.html',context)
    # except:
    #     return redirect('')


def addcomment(request,slug):
    if not request.user.is_authenticated:
        return HttpResponse('You are not logged in !')
    try:
        if request.method=='POST':
            post=Post.objects.get(slug=slug)
            user=request.user
            content=request.POST['content']
            new_comment=Comment(user=user,post=post,content=content)
            new_comment.save()
            return HttpResponse('Comment added successfully')
        else:
            return HttpResponse('Something went wrong')
    except:
        return HttpResponse('Something went wrong')
    
def addreply(request,slug):
    try:
        if request.method=='POST':
            post=Post.objects.get(slug=slug)
            user=request.user
            content=request.POST['content']
            parent_id=request.POST['parent']
            comment=Comment.objects.get(id=parent_id)
            new_comment=Comment(user=user,post=post,content=content,parent=comment)
            new_comment.save()
            return HttpResponse('Comment added successfully')
        else:
            return HttpResponse('Something went wrong')
    except:
        return HttpResponse('Something went wrong')
    
def likePost(request,slug):
    try:
        if not request.user.is_authenticated:
            post=Post.objects.get(slug=slug)
            return JsonResponse({'likes':len(post.likes.all()),'user':0})
        else:
            user=request.user
            post=Post.objects.get(slug=slug)
            if(post.likes.contains(user)):
                post.likes.remove(user)
                return JsonResponse({'likes':len(post.likes.all()),'user':1})
            elif(not post.likes.all().contains(user)):
                post.likes.add(user)
                return JsonResponse({'likes':len(post.likes.all()),'user':1})
            else:
                return JsonResponse({'likes':len(post.likes.all()),'user':0})
    except:
        return JsonResponse({'likes':len(post.likes.all()),'user':0})
    
    
    
   
    
def posts_by_cat(request,category):
    tags=Tag.objects.all()
    cat_array=category.split('-')
    cat=' '.join(cat_array)
    context={
        'tags':tags,
        'category':category,
        'cat':cat
    }
    return render(request,'posts/posts_by_cat.html',context)

@api_view(['GET'])
def getHeaderPost(request):
    if request.method=='GET':
        # get the table of header from database.
        header_post_ids=HeaderPosts.objects.get(id=1)
        header_serializer=HeaderPostSerializer(header_post_ids)
        post_list=[]
        header_left=Post.objects.get(pk=header_serializer.data.get('header_left'))
        serializer=PostSerializer(header_left)
        post_list.append(serializer.data)
        
        header_right_top=Post.objects.get(pk=header_serializer.data.get('header_right_top'))
        serializer=PostSerializer(header_right_top)
        post_list.append(serializer.data)
        
        header_right_bottom_left=Post.objects.get(pk=header_serializer.data.get('header_right_bottom_left'))
        serializer=PostSerializer(header_right_bottom_left)
        post_list.append(serializer.data)
        header_right_bottom_right=Post.objects.get(pk=header_serializer.data.get('header_right_bottom_right'))
        serializer=PostSerializer(header_right_bottom_right)
        post_list.append(serializer.data)
        return Response(post_list)
    
@api_view(['GET'])
def popular_posts(request):
    posts=Post.objects.annotate(like_count=Count('likes')).order_by('-like_count')[0:5]
    serializer=PostSerializer(posts,many=True)
    return Response({'data':serializer.data})


def search_posts(request):
    tags=Tag.objects.all()
    context={
        'tags':tags
    }
    return render(request,'posts/search_posts.html',context)



@api_view(['GET'])
def load_search_posts(request):
    search_query=request.GET.get('search')
    page_number=request.GET.get('page')
    if search_query!='' and search_query!=None:
        posts=Post.objects.filter(title__icontains=search_query)[8*(int(page_number)-1):8*(int(page_number)-1)+8]
        total_posts=Post.objects.filter(title__icontains=search_query).count()
        serializer=PostSerializer(posts,many=True)
        return Response({'data':serializer.data,'total_posts':total_posts})
    else:
        return Response({'data':'Data not found','total_posts':0}) 
    
def liked_posts(request):
    if not request.user.is_authenticated:
        return redirect('home')
    tags=Tag.objects.all()
    context={
        'tags':tags
    }
    return render(request,'posts/liked_posts.html',context)

@api_view(['GET'])
def load_liked_posts(request):
    if not request.user.is_authenticated:
        return redirect('home')
    try:
        page_number=request.GET.get('page')
        user=request.user
        posts=Post.objects.filter(likes=user)[8*(int(page_number)-1):8*(int(page_number)-1)+8]
        total_posts=Post.objects.filter(likes=user).count()
        serializer=PostSerializer(posts,many=True)
        return Response({'data':serializer.data,'total_posts':total_posts})
    except:
        return Response({'data':[],'total_posts':0})

# comment --------------------
@api_view(['GET'])
def comments(request,post_slug):
    try:
        post=Post.objects.get(slug=post_slug)
        comments=Comment.objects.filter(post=post,parent=None)
        serializer=CommentSerializer(comments,many=True)
        return Response({'data':serializer.data})
    except:
        return Response({'data':[]})

@api_view(['GET'])
def load_replies(request,post_slug,comment_id):
    try:
        post=Post.objects.get(slug=post_slug)
        comment=Comment.objects.get(id=comment_id)
        comments=Comment.objects.filter(post=post,parent=comment)
        serializer=CommentSerializer(comments,many=True)
        return Response({'data':serializer.data})
    except:
        return Response({'data':[]})
    