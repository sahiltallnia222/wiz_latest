from django.contrib.sitemaps import Sitemap
from posts.models import Post
from django.urls import reverse

class PostSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8
    protocol = 'https'

    def items(self):
        return Post.objects.all()

    def lastmod(self, obj):
        return obj.modified_date
        
    def location(self,obj):
        return '/posts/post/%s' % (obj.slug)

    
    

class StaticSitemap(Sitemap):
    changefreq = "yearly"
    priority = 0.8
    protocol = 'https'

    def items(self):
        return ['home','load_posts']

    def location(self, item):
        return reverse(item)