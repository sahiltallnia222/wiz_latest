from django.contrib import admin
from .models import Post,Comment,Tag,HeaderPosts
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    readonly_fields=('id',)

class HeaderAdmin(admin.ModelAdmin):
    readonly_fields=('id',)

admin.site.register(Post,PostAdmin)
admin.site.register(Comment)
admin.site.register(Tag)
admin.site.register(HeaderPosts,HeaderAdmin)


