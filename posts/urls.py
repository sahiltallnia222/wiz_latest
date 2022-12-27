
from django.urls import path

from . import views

app_name='posts'

urlpatterns = [
    path('post/<slug:slug>/',views.post_details,name='post_details'),
    path('comments/<slug:post_slug>/',views.comments,name='load_comments'),
    path('replies/<slug:post_slug>/<slug:comment_id>',views.load_replies,name='load_replies'),
    path('addcomment/<slug:slug>/',views.addcomment,name='add_comment'),
    path('addreply/<slug:slug>/',views.addreply,name='add_reply'),
    path('likepost/<slug:slug>/',views.likePost,name='like_post'),
    path('category/<slug:category>/',views.posts_by_cat, name='posts_by_cat'),
    path('load_cat_posts/<slug:category>/',views.load_cat_posts,name='load_cat_posts'),
    path('header-posts/get-id-post/',views.getHeaderPost,name='get-id-post'),
    path('popular-posts/',views.popular_posts,name='popular_posts'),
    path('search-posts/',views.search_posts,name='search_posts'),
    path('liked-posts/',views.liked_posts,name='liked_posts'),
    path('load-liked-posts/',views.load_liked_posts,name='load-liked_posts'),
    path('load_search_posts/',views.load_search_posts,name='load_search_posts'),
]