from django.contrib import admin

# Register your models here.

from .models import ToDo, Executor


class ToDoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'executor',
                    'period_of_execution', 'is_complete')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_complete',)
    list_filter = ('is_complete', 'executor')


class ExecutorAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)


admin.site.register(ToDo, ToDoAdmin)
admin.site.register(Executor, ExecutorAdmin)
