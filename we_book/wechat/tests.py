from django.test import TestCase

# Create your tests here.
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.core.paginator import Paginator
import requests
import time
from wechat.models import Book,UserInfo,bookcollect,Task

import re
import json
import base64


def set_task(request):
    s_id = request.session['id']
    print(s_id)
#     判断这个人是老师还是学生
    p = UserInfo.objects.get(id=s_id)
    p_type = p.type
    if p_type:
        # 判断是老师，发布任务
        Class = request.POST.get("Class")
        title = request.POST.get("title")
        end_time = request.POST.get("time")
        result = Task.objects.create(Class = Class,title=title,end_time=end_time)
        data = {
            'Class': result.Class,
            'title': result.title,
            'end_time': result.end_time,
        }
        return HttpResponse(json.dumps({'data': data}), content_type="application/json")
    else:
        s_id = request.session['id']
        p = UserInfo.objects.get(id=s_id)
        try:
            task = Task.objects.get(Class=p.Class)
            title = task.title
            end_time = task.end_time
            data = {
                'title':title,
                'end_time':end_time,
            }
            return HttpResponse(json.dumps({'data': data}), content_type="application/json")
        except:
            return HttpResponse(json.dumps({'data': '没有任务'}), content_type="application/json")





