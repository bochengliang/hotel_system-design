from django.db import models
# Create your models here.
from django.db import models
class Admin_info(models.Model):
    name = models.CharField('管理员名字',max_length=100,primary_key=True)
    password = models.CharField('密码',max_length=100,null=False)
    role = models.CharField('角色',max_length=100,null=False)
    # add_room = models.IntegerField('添加房间',null=False)
    def __str__(self):
        return self.name

class Room_kind(models.Model):
    add_room1 = models.IntegerField('大床房', null=False,default='')
    add_room2 = models.IntegerField('情侣房', null=False,default='')
    add_room3 = models.IntegerField('海底房', null=False,default='')
    add_room4 = models.IntegerField('三人房', null=False,default='')
    add_room5 = models.IntegerField('双人房', null=False,default='')
    add_room6 = models.IntegerField('单人房', null=False,default='')

class Room_info(models.Model):
    num = models.CharField('编号',max_length=100,primary_key=True)
    price = models.IntegerField('价格')
    kind = models.CharField('类型',max_length=100,null=False)    # room_kind = models.CharField('房型',max_length=100,default=' ')

    status = models.CharField('状态',max_length=100,null=False,editable=True)

class Customer_info(models.Model):
    name = models.CharField('顾客名字',max_length=100)
    phone = models.CharField('手机号',max_length=11,null=False)
    id_card = models.CharField('证件号',max_length=100,null=False,primary_key=True)

class Comment_info(models.Model):
    Name = models.CharField('顾客名字',max_length=100)
    Email = models.EmailField('邮箱',max_length=30)
    number = models.CharField('手机号',max_length=11,primary_key=True)
    Message = models.TextField('内容',max_length=41,null=False)
    pub_date = models.DateTimeField('发表时间', auto_now_add=True, editable=True)