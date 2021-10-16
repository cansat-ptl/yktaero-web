from django.contrib import admin
from .models import Tag, Post, Project, Item, Feedback


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    pass


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("sku",)}


@admin.register(Feedback)
class ItemAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)

