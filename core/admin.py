from django.contrib import admin
from .models import User, Post, Comment, Tag
from django.contrib.admin import AdminSite

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Post Details', {
            'fields':('user','title', 'subtitle', 'body', 'tag',),
        }),
        ('Image(s)',{
            'fields':('post_img',),
            'description': "Attached image(s)"
        }),
    )

    list_display = ['user', 'title', 'created']
    list_display_links = ('title',)


admin.site.register(User)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
admin.site.register(Tag)