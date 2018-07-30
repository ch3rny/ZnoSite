from django.contrib import admin
from .models import Review


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('author', 'created_time', 'text', 'unread')
    date_hierarchy = 'created_time'


admin.site.register(Review, ReviewAdmin)
