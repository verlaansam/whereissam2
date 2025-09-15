from django.contrib import admin
from .models import Post, Category, WindSpeed, WindDirection, Seastate

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(WindSpeed)
class WindSpeedAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(WindDirection)
class WindDirectionAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Seastate)
class SeastateAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'windspeed', 'winddirection', 'seastate', 'created_at', 'image')
    list_filter = ('categories', 'windspeed', 'winddirection', 'seastate', 'author', 'created_at')
    search_fields = ('title', 'content')
