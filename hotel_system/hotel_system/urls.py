from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.urls import path, re_path
from myapp import views
urlpatterns = [
    path('',views.index),
    path('admin/', admin.site.urls),#管理员网页
    re_path('services/$',views.show_rooms),#预定页面
    re_path('single/$',views.show_coment),#评论页面
    re_path('index/$',views.index),#主页
    re_path('services/Ording/$',views.Ording),
    re_path('add/$',views.add_to_database),#预定信息添加到数据库
    re_path('add/comment/$',views.add_comment),#评论到数据库
    re_path('ensure/$',views.ensure),
    re_path('ording_room1/$',views.ording_room1),
    re_path('ording_room2/$',views.ording_room2),
    re_path('ording_room3/$',views.ording_room3),
    re_path('ording_room4/$',views.ording_room4),
    re_path('ording_room5/$',views.ording_room5),
    re_path('ording_room6/$',views.ording_room6),
    re_path('more_info1/$',views.more_info1),
    re_path('more_info2/$',views.more_info2),
    re_path('more_info3/$',views.more_info3),

]