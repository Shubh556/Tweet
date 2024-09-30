from django.contrib import admin
from .models import Tweet
from django.contrib.auth.models import User

class TweetAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at', 'is_user_active')

    def is_user_active(self, obj):
        return obj.user.is_active
    
    is_user_active.short_description = 'Is User Active'
    is_user_active.boolean = True

admin.site.register(Tweet, TweetAdmin)
