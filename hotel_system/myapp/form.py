from django.forms import Form
from django.forms import fields
from django.forms import widgets
from .models import *


# class UserForm(Form):
#     username = fields.CharField(
#         required=True,       #规定该字段不能为空
#         error_messages={'required':'名字不能为空'}     # 自定义错误信息，'required'是定义该字段为空时的错误信息
#     )
#     password = fields.CharField(
#         required=True,
#         error_messages={'required':'身份证不能为空'}
#     )
#     number = fields.CharField(
#         required=True,
#         error_messages={'required': '手机号不能为空'}
#     )
#     # email = fields.EmailField(
#     #     required=True,
#     #     error_messages={'required':'邮箱不能为空','invalid':'邮箱格式错误'}
#     # )
