from django.contrib import admin
from testapp.models import Post, Comment,UserProfile
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display=['title','author','id','total_likes']

class CommentAdmin(admin.ModelAdmin):
    list_display=['post','post_id','id']

class UserProfileAdmin(admin.ModelAdmin):
    list_display=['id','user_id','bio']



admin.site.register(Post,PostAdmin)
admin.site.register(Comment,CommentAdmin)
admin.site.register(UserProfile,UserProfileAdmin)
