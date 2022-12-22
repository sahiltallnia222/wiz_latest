from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('privacy-policy',views.privacy_policy),
    path('load_posts/',views.load_posts,name='load_posts'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path("admin/", admin.site.urls),
    path('accounts/',include('accounts.urls')),
    path('posts/',include('posts.urls')),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)