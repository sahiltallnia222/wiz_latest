from rest_framework import serializers
from posts.models import Post,Tag

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model=Tag
        fields='__all__'

class PostSerializer(serializers.ModelSerializer):
    tags=TagSerializer(source='tag',many=True)
    class Meta:
        model=Post
        fields=['id','title','content','likes','slug','thumbnail','tags','category','created_date','modified_date']