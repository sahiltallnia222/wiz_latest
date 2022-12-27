from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from .sitemaps import StaticSitemap,PostSitemap,PostCatSitemap
from django.views.generic.base import TemplateView

from . import views
sitemaps = {
    'static':StaticSitemap,
    'posts':PostSitemap,
    'cat_posts':PostCatSitemap
}

urlpatterns = [
     path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('',views.home,name='home'),
    path('privacy-policy/',views.privacy_policy,name='privacy_policy'),
    path('load_posts/',views.load_posts,name='load_posts'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path("admin/", admin.site.urls),
    path('accounts/',include('accounts.urls')),
    path('posts/',include('posts.urls')),
     path(
        "robots.txt",
        TemplateView.as_view(template_name="robots.txt", content_type="text/plain"),
    ),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)