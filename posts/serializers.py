from rest_framework import serializers
from posts.models import Post,Tag,HeaderPosts,Comment
from accounts.models import User
class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model=Tag
        fields='__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields='__all__'

class PostSerializer(serializers.ModelSerializer):
    tags=TagSerializer(source='tag',many=True)
    cat=serializers.SerializerMethodField()
    class Meta:
        model=Post
        fields=['id','title','content','likes','slug','thumbnail','tags','category','cat','created_date','modified_date']
        
    def get_cat(self,obj):
        return {'cat':obj.get_category_display()}
        
class HeaderPostSerializer(serializers.ModelSerializer):
    class Meta:
        model=HeaderPosts
        fields='__all__'
        
class CommentSerializer(serializers.ModelSerializer):
    userdetails=UserSerializer(source='user')
    children=serializers.SerializerMethodField()
    class Meta:
        model=Comment
        fields=['id','parent','post','userdetails','content','created_date','children']
    def get_children(self,obj):
        return len(obj.children)