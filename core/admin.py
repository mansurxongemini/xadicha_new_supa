from django.contrib import admin
from .models import Biography, Book, VideoResource, ProjectAuthor, ScientificArticle, NewsBlog


# Register your models here.
@admin.register(Biography)
class BiographyAdmin(admin.ModelAdmin):
    list_display = ('title',)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title',)

@admin.register(VideoResource)
class VideoResourceAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'embed_code')

@admin.register(ProjectAuthor)
class ProjectAuthorAdmin(admin.ModelAdmin):
    list_display = ('full_name',)

@admin.register(ScientificArticle)
class ScientificArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'publication_source', 'published_date')

@admin.register(NewsBlog)
class NewsBlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('title', 'content')
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)
    readonly_fields = ('created_at',)   