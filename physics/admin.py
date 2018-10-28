from django.contrib import admin
from .models import Theme, Task, Bundle
# Register your models here.


class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'year', 'number', 'theme', 'zno_type', 'type')
    list_filter = ('year', 'theme', 'zno_type', 'type')


admin.site.register(Task, TaskAdmin)
admin.site.register(Theme)
admin.site.register(Bundle)


