from django.contrib import admin
from .models import *
# Register your models here.


class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'year', 'number', 'theme', 'zno_type', 'type')
    list_filter = ('year', 'theme', 'zno_type', 'type')


class TestAnswerAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'theme', 'date', 'user_answer', 'is_true')
    list_filter = ('user', 'theme', 'date', 'is_true')


admin.site.register(Task, TaskAdmin)
admin.site.register(Theme)
admin.site.register(Bundle)
admin.site.register(TestAnswer, TestAnswerAdmin)


