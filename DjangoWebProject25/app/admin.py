from django.contrib import admin

# Register your models here.

from .models import Post
class PostModelAdmin(admin.ModelAdmin):
    list_display = ["title", "updated", "timestamp"]
    list_display_Links = ["updated"]
   # list_editable = ["title"]
    list_filter = ["updated", "timestamp"]
    seach_filter = ["title", "content"]
    class Meta:
        model = Post

admin.site.register(Post, PostModelAdmin)


#admin.site.register(Post)