from django.contrib import admin

from .models import Movie, Actor, Director, Category, Genera, Writter, Comment

class MovieAdmin(admin.ModelAdmin):
    list_display  = ('title', 'year', 'category')
    search_fields = ('title', 'year')
    list_filter   = ('title', 'author', 'time')


admin.site.register(Movie, MovieAdmin)

class ActorAdmin(admin.ModelAdmin):
    list_display  = ('name', 'born', 'died')
    search_fields = ('name',)
    list_filter   = ('name', 'born')


admin.site.register(Actor, ActorAdmin)


admin.site.register(Director)
class CategoryAdmin(admin.ModelAdmin):
    list_display  = ('name',)
    search_fields = ('name',)
    list_filter   = ('name',)

admin.site.register(Category, CategoryAdmin)
admin.site.register(Genera)
admin.site.register(Writter)

class CommentAdmin(admin.ModelAdmin):
    list_display  = ('post', 'author', 'created_on',)
    search_fields = ('post',)
    list_filter   = ('post',)

admin.site.register(Comment, CommentAdmin)
