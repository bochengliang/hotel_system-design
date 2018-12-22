from django.contrib import admin
from myapp.models import *

class room_kind(admin.ModelAdmin):
    list_display = ['add_room1','add_room2','add_room3','add_room4','add_room5','add_room6']
admin.site.register(Room_kind,room_kind)
class admin_infos(admin.ModelAdmin):
    list_display = ['name','password','role']
admin.site.register(Admin_info,admin_infos)

class  room_info(admin.ModelAdmin):
    list_display = ['num','price','kind','status']
admin.site.register(Room_info,room_info)

class  customer_info(admin.ModelAdmin):
    list_display = ['name','phone','id_card',]

admin.site.register(Customer_info,customer_info)

class comment_info(admin.ModelAdmin):
    list_display = ['pub_date','Name','Email','number','Message']
    ordering = ('-pub_date',)

admin.site.register(Comment_info,comment_info)




