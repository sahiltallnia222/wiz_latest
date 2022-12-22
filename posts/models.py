from email.policy import default
from django.db import models
from django.template.defaultfilters import slugify
from accounts.models import User
from tinymce.models import HTMLField
from ckeditor_uploader.fields import RichTextUploadingField
import uuid

class Tag(models.Model):
    
    tag=models.CharField(max_length=50)
    
    def __str__(self):
        return self.tag
    
    
class Post(models.Model):
    POST_CATEGORIES=(
        ('education','Education'),
        ('science-and-technology','Science and Tech'),
        ('finance','Finance'),
    )
    user=models.ForeignKey(User,related_name='user_post',on_delete=models.CASCADE)
    title=models.CharField(max_length=250)
    content=RichTextUploadingField()
    category=models.CharField(choices=POST_CATEGORIES,max_length=50,default='education')
    slug = models.SlugField(max_length = 250, null = True, blank = True)
    thumbnail=models.ImageField(upload_to='post_thumbnails',blank=True,null=True)
    created_date=models.DateTimeField(auto_now_add=True)
    modified_date=models.DateTimeField(auto_now=True)
    likes=models.ManyToManyField(User,related_name='user_like',blank=True)
    tag=models.ManyToManyField(Tag,related_name='tag_post',blank=True)
    rec_posts=models.CharField(max_length=250,default='1-2-3')
    desc=models.TextField(max_length=255,blank=True,null=True)
    keywords=models.TextField(max_length=255,blank=True,null=True)
    def __str__(self):
        return self.title
    
    
class Comment(models.Model):
    user=models.ForeignKey(User,related_name='user_comment',on_delete=models.CASCADE)
    post=models.ForeignKey(Post,related_name='post_comment',on_delete=models.CASCADE)
    content=models.TextField()
    created_date=models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey('self' , null=True , blank=True , on_delete=models.CASCADE , related_name='replies')

    @property
    def children(self):
        return Comment.objects.filter(parent=self).reverse()

    @property
    def is_parent(self):
        if self.parent is None:
            return True
        return False

    def __str__(self):
        return self.user.username
    
    
    
class HeaderPosts(models.Model):
    header_left=models.IntegerField(default=1)
    header_right_top=models.IntegerField(default=2)
    header_right_bottom_left=models.IntegerField(default=3)
    header_right_bottom_right=models.IntegerField(default=4)
    def __str__(self):
        return 'Header Posts'
    
    
