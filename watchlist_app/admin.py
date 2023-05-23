from django.contrib import admin
from .models import WatchList, StreamPlatform
# Register your models here.
# @admin.register(Page)
# class PageAdmin(admin.ModelAdmin):
#    list_display=['page_name','page_cat','page_publish_date','user']
admin.site.register(WatchList)
admin.site.register(StreamPlatform)

