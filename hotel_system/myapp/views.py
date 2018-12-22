from django.shortcuts import render,render_to_response
from myapp.models import *
from myapp import *
from myapp.form import *
from django.core import validators
from django.forms import CharField
from django.views.decorators.cache import cache_page
#引入这个HttpResponse包，它可以把响应内容返回，这样客户端就可以得到响应内容。
from django.core.paginator import Paginator

def index(request):
    return render(request,'index.html')
def services(request):
    return render(request,"services.html")
def single(request):
    return render(request,"single.html")
def ensure(request):
    return render(request,"ensure.html")

global val  #在使用前初次声明
val = 10
def ording_room1(request):
    global val
    Room_kind.objects.filter(id=1).update(add_room1=val-1)

    val=val-1
    if val <= 0:
        message = "FailedMsgBox()"
    else:
        message = "SuccessMsgBox()"
        return render(request, 'Ording.html',{"message":message})

global val1  #在使用前初次声明
val1 = 10
def ording_room2(request):
    global val1
    # Customer_info.objects.update(room_kind='情侣房')
    Room_kind.objects.filter(id=1).update(add_room2=val1-1)

    val1=val1-1
    if val <= 0:
        message = "FailedMsgBox()"
    else:
        message = "SuccessMsgBox()"
        return render(request, 'Ording.html',{"message":message})
global val2  #在使用前初次声明
val2 = 10
def ording_room3(request):
    global val2
    # Costum = Customer_info()
    # Costum.room_kind = '海底房'
    # Customer_info.objects.filter(id=3).update(add_room3='海底房')
    Room_kind.objects.filter(id=1).update(add_room3=val2-1)

    val2=val2-1
    if val2 <= 0:
        message = "FailedMsgBox()"
    else:
        message = "SuccessMsgBox()"
        return render(request, 'Ording.html',{"message":message})

global val3  #在使用前初次声明
val3 = 10
def ording_room4(request):
    global val3
    # Costum = Customer_info()
    # Costum.room_kind = '三人房'
    # Costum.save()
    Room_kind.objects.filter(id=1).update(add_room4=val3-1)

    val3=val3-1
    if val <= 0:
        message = "FailedMsgBox()"
    else:
        message = "SuccessMsgBox()"
        return render(request, 'Ording.html',{"message":message})
global val4  #在使用前初次声明
val4 = 10
def ording_room5(request):
    global val4
    # Costum = Customer_info()
    # Costum.room_kind = '双人房'
    # Costum.save()
    Room_kind.objects.filter(id=1).update(add_room5=val4-1)

    val4=val4-1
    if val4 <= 0:
        message = "FailedMsgBox()"
    else:
        message = "SuccessMsgBox()"
        return render(request, 'Ording.html',{"message":message})


global val5  #在使用前初次声明
val5 = 10
def ording_room6(request):
    global val5
    # Costum = Customer_info()
    # Costum.room_kind = '单人房'
    # Costum.save()
    Room_kind.objects.filter(id=1).update(add_room6=val5-1)

    val5=val5-1
    if val <= 0:
        message = "FailedMsgBox()"
    else:
        message = "SuccessMsgBox()"
        return render(request, 'Ording.html',{"message":message})



def Ording(request):
    return render(request,"Ording.html")


def more_info1(request):
    return render(request,"more_info1.html")
def more_info2(request):
    return render(request,"more_info1.html")

def more_info3(request):
    return render(request,"more_info1.html")



def add_to_database(request):
    if request.method == "POST":
        username = request.POST['username']
        id_card = request.POST['id_card']
        number = request.POST['number']


        Costum = Customer_info()
        Costum.name = username
        Costum.id_card = id_card
        Costum.phone = number
        Costum.save()
    else:
        username = request.GET['username']
        id_card = request.GET['id_card']
        number = request.GET['number']
    mes = '恭喜你，预定成功！'
    return render(request,'Index.html')

    #校验函数
    #     username = request.POST['username']
    #     id_card = request.POST['id_card']
    #     number = request.POST['number']
    # if request.method == "GET":
    #     form = UserForm()
    #     return render(request, 'login.html', {'form': form})
    #
    # elif request.method == 'POST':
    #     form = UserForm()
    #     form = UserForm(data=request.POST)
    #     # 将前端获取的数据传入到forms.UserForm类，实例化得到一个包含字段值的表单对象form
    #     if form.is_valid():  # is_valid()得到一个布尔值，判断传入的字段值是否全部有效
    #         print(form.cleaned_data)  # form.cleaned_data是字典类型，得到全部字段的有效值，即干净的数据
    #         Customer_info.objects.create(**form.cleaned_data)  # 直接插入数据库，form字段必须与models中定义的一致
    #
    #     else:
    #         print(form.errors)  # 得到错误信息，并生成html标签，哪个字段值有误，就会对应产生哪个字段的错误信息
    #         return render(request, 'Ording.html', locals())

def show_rooms(request):
    Room=Room_info.objects.all()    #获取我们的数据库信息到names里
    return render(request,"services.html",{"Room":Room}) #必须用这个return

#评论信息
@cache_page(60 * 15) # 秒数，这里指缓存 15 分钟，不直接写900是为了提高可读性
def show_coment(request):
    comments = Comment_info.objects.all()  # 获取全部数据
    limit = 3
    paginator = Paginator(comments, limit)
    page = request.GET.get('page', '1')
    result = paginator.page(page)
    return render(request,'single.html',{"comments":result})


def add_comment(request):
    if request.method=='POST':
        Name = request.POST['Name']
        Email = request.POST['Email']
        number = request.POST['Phone number']
        Message= request.POST['Message']

    else:
        Name = request.GET['Name']
        Email = request.GET['Email']
        number = request.GET['Phone number']
        Message= request.GET['Message']

    Comment = Comment_info()
    Comment.Name = Name
    Comment.Email = Email
    Comment.number = number
    Comment.Message = Message
    Comment.save()

    return render(request,"index.html")

