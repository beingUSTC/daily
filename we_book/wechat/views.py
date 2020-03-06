from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.core.paginator import Paginator
import requests
from wechat.models import Book,UserInfo,bookcollect,Task

import re
import json
import base64

# Create your views here.

def register(request):
    if request.method == 'GET':
        # 显示注册页面
        return render(request, 'register.html')
    else:
        Username = request.POST.get('username')
        password = request.POST.get('password')
        type = request.POST.get('type')
        Class = request.POST.get('Class')
        if not all([Username, password, type, Class]): # 数据不完整
            return render(request, 'register.html', {'errmsg': '数据不完整'})
        try:
            user = UserInfo.objects.get(username=Username)
        except UserInfo.DoesNotExist:
            # 用户名不存在
            user = None

        if user:
            # 用户名已存在
            return render(request, 'register.html', {'errmsg': '用户名已存在'})
        result = UserInfo.objects.create(username=Username, password=password, type=type, Class=Class)
        data = {
            'userid': result.id,
            'username': result.username,
            'password': result.password,
            'type': result.type,
            'class': result.Class,
        }
        return HttpResponse(json.dumps({'data':data}),content_type="application/json")


def login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    if not all([username, password]):
        return render(request, 'login.html', {'errmsg': '数据不完整'})

    result = UserInfo.objects.get(username=username, password=password)
    if result.username==username:
        data = {
            'userid': result.id,
            'username': result.username,
            'password': result.password,
            'type': result.type,
            'class': result.Class,
        }
        request.session['id'] = result.id
        request.session['username'] = result.username
        request.session['password'] = result.password
        request.session['type'] = result.type
        request.session['Class'] = result.Class
    else:
        # 可以细分错误类型比如密码错误
        return render(request, 'login.html', {'errmsg': 'wrong'})
    return HttpResponse(json.dumps({'result': 1, 'data': data}), content_type="application/json")


def search_book(request):
    # 得到书名，查找图书，如果登录则看是否已经收藏
    title = request.POST.get('data')
    # title = '百科全书'
    print(title)
    # print(type(title))
    book = Book.objects.get(title=title)
    # 得到书籍
    sessionid = request.COOKIES.get('sessionid')
    # 得到用户信息 改为名字
    # s = session.objects.get(session_key = sessionid)
    s_id = request.session['id']
    # str = base64.b64decode('s.session_data').decode("utf-8")
    # str_id = re.findall(r'id":(.*?),"',str)[0]

    if sessionid:
        try:
            b_collect = bookcollect.objects.get(userid=s_id,bookid=book.id)
            info = {
                'book_title':book.title,
                'info': 'have collect',
            }
        except Exception as e:
            return HttpResponse(json.dumps({'data': {'book_title':book.title,'book':book.location,
            'info':'no collect'}}), content_type="application/json")
    else:
        info = {
            'book_title': book.title,
            'errmsg': 'no login',
        }
    # 如果点击收藏则存入数据库
    url = book.location
    data = {
        'book_title': book.title,
        'book_location': url,
        'info':info,
    }
    return HttpResponse(json.dumps({'data': data}), content_type="application/json")


def add_favorite(request):
    userid = request.COOKIES.get('sessionid')
    if userid:
        bookname = request.POST.get['title']
        result = Book.objects.get(title=bookname)
        bookcollect.objects.create(bookid=result.id, userid=userid)
        return HttpResponse('收藏成功')
    else:
        return render(request, 'login.html', {'errmsg': 'you need login'})


def task(request):
    # s_id = request.session['id']
    # print(s_id)
#     判断这个人是老师还是学生
#     p = UserInfo.objects.get(id=s_id)
#     p_type = p.type
#     if p_type:
        # 判断是老师，发布任务
        Class = request.POST.get("c")
        title = request.POST.get("title")
        end_time = request.POST.get("time")
        result = Task.objects.create(Class = Class,title=title,dateline=end_time)
        # result = Task.objects.create(Class=1, title='baike', dateline="2129-1-1")
        data = {
            'Class': result.Class,
            'title': result.title,
            'end_time': result.dateline,
        }
        return HttpResponse(json.dumps({'data': data}), content_type="application/json")
    # else:
    #     s_id = request.session['id']
    #     p = UserInfo.objects.get(id=s_id)
    #     try:
    #         task = Task.objects.get(Class=p.Class)
    #         title = task.title
    #         end_time = task.end_time
    #         data = {
    #             'title':title,
    #             'end_time':end_time,
    #         }
    #         return HttpResponse(json.dumps({'data': data}), content_type="application/json")
    #     except:
    #         return HttpResponse(json.dumps({'data': '没有任务'}), content_type="application/json")



'''
def login_yemian(request):
    Username = request.POST.get('username')
    password = request.POST.get('password')
    data = {
        'username': Username,
        'password':password,
    }
    print(data)
    return render(request, 'login.html', {'data': data})

def login(request):
    re = login_yemian()
    print(re)
    Username = request.POST.get('username')
    password = request.POST.get('password')
    print(1)
    try:
        result = UserInfo.objects.get(username=Username, password=password)
        result.set_cookie('username', 'password')
        print(2)
        data = {
            'userid':result.id,
            'username':result.username,
            'password':result.password,
            'type':result.type,
            'class':result.Class,
        }
        # return HttpResponse(json.dumps({'result': 1, 'data': data}), content_type="application/json")
        print(data)
        return render(request, 'login.html', {'data': data})
    except Exception as e:
        print(e)
        return HttpResponse(json.dumps({'result': 0}), content_type="application/json")
def index(request):
    response = HttpResponse("index")
    response.set_cookie('username','123456')
    return response

def my_list(request):
    cookies = request.COOKIES
    username = cookies.get('username')
    return HttpResponse(username)

def session_view(request):
    username = request.session.get('username')#用于请求session中的数据

    request.session['username'] = 'yzy'#用于设置session
    return HttpResponse('session ')
'''





