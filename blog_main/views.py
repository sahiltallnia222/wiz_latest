from django.shortcuts import render
from posts.models import Post,Tag
from rest_framework.decorators import api_view
from .serializers import PostSerializer
from rest_framework.response import Response


def home(request):
    total_posts=Post.objects.count()
    tags=Tag.objects.all()
    context={
        'total_posts':total_posts,
        'tags':tags,
    }
    return render(request,'home.html',context)



@api_view(['GET'])
def load_posts(request):
    if(request.method=='GET'):
        page_number=request.GET.get('page')
        tag_value=request.GET.get('tag')
        if tag_value:
            try:
                tag=Tag.objects.get(tag__exact=tag_value)
                load_posts=Post.objects.filter(tag=tag).order_by('-modified_date')[8*(int(page_number)-1):8*(int(page_number)-1)+8]
                total_posts=Post.objects.filter(tag=tag).count()
                serializer=PostSerializer(load_posts,many=True)
                return Response({'data':serializer.data,'total_posts':total_posts})
            except:
                total_posts=0
                return Response({'data':[],'total_posts':total_posts})
        else:
            load_posts=Post.objects.all().order_by('-modified_date')[8*(int(page_number)-1):8*(int(page_number)-1)+8]
            total_posts=Post.objects.count()
            serializer=PostSerializer(load_posts,many=True)
            return Response({'data':serializer.data,'total_posts':total_posts})



def privacy_policy(request):
    return render(request,'privacypolicy.html')

