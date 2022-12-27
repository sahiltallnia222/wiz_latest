from django.contrib.sitemaps import Sitemap
from posts.models import Post
from django.urls import reverse

class PostSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.8
    protocol = 'https'

    def items(self):
        return Post.objects.all().order_by('-modified_date')

    def lastmod(self, obj):
        return obj.modified_date
        
    def location(self,obj):
        return '/posts/post/%s/' % (obj.slug)

class PostCatSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.8
    protocol = 'https'

    def items(self):
        return Post.POST_CATEGORIES

        
    def location(self,obj):
        return '/posts/category/%s/' %(obj[0])
    

class StaticSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.8
    protocol = 'https'

    def items(self):
        return ['home','privacy_policy','posts:popular_posts']

    def location(self, item):
        return reverse(item)
    def priority(self, item):
        return {'home':1.0,'privacy_policy':0.8,'posts:popular_posts':0.8}[item]