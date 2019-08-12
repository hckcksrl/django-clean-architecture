from django.contrib import admin
from .models import model

@admin.register(model.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'content',
        'created_at',
        'updated_at',
        'author'
    )
    list_display_links = (
        'title',
        'author'
    )


# Register your models here.
