
from django.contrib import admin
from notify.models import *
# Register your models here.
class NodeAdmin(admin.ModelAdmin):
    list_display = ('nodename', 'nodeip','nodeinfo')
    fields = ['nodename', 'nodeip','nodeinfo']

class UserRecordsAdmin(admin.ModelAdmin):
    list_display = ('userid','starttime','endtime','lemo')
    fields = ['userid','starttime','endtime','lemo']

admin.site.register(Node,NodeAdmin)
admin.site.register(UserRecords,UserRecordsAdmin)