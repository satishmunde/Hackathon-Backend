from django.contrib import admin
from .models import Community, CommunityMembership, Post, Comment, Like, ModerationAction

# Inline for managing CommunityMemberships directly within Community admin
class CommunityMembershipInline(admin.TabularInline):
    model = CommunityMembership
    extra = 1  # Number of empty membership rows to display by default
    fields = ('user', 'role', 'joined_at')
    readonly_fields = ('joined_at',)
    autocomplete_fields = ['user']  # Helps with searching users if there are many

# Community Admin
class CommunityAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_by', 'created_at')  # Show these fields in list view
    search_fields = ('name', 'description')  # Search by name or description
    list_filter = ('created_at',)  # Filter by creation date
    inlines = [CommunityMembershipInline]  # Show the inline community memberships

# Post Admin
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'community', 'created_at', 'updated_at')
    search_fields = ('title', 'content')
    list_filter = ('created_at', 'community')
    autocomplete_fields = ['author', 'community']  # Helps with dropdown lists

# Comment Admin
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'author', 'created_at', 'parent')
    search_fields = ('content',)
    list_filter = ('created_at', 'post')
    autocomplete_fields = ['author', 'post', 'parent']  # Helps with nested comments

# Like Admin
class LikeAdmin(admin.ModelAdmin):
    list_display = ('user', 'post', 'comment', 'created_at')
    autocomplete_fields = ['user', 'post', 'comment']  # Helps with user and post/comment selection

# ModerationAction Admin
class ModerationActionAdmin(admin.ModelAdmin):
    list_display = ('moderator', 'community', 'action', 'created_at')
    search_fields = ('reason',)
    list_filter = ('action', 'created_at', 'community')
    autocomplete_fields = ['moderator', 'community', 'target_post', 'target_comment', 'target_user']  # Helps with dropdown lists

# Register all the models in the admin panel
admin.site.register(Community, CommunityAdmin)
admin.site.register(CommunityMembership)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Like, LikeAdmin)
admin.site.register(ModerationAction, ModerationActionAdmin)
