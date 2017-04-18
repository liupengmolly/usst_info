# coding: utf8
from django.shortcuts import render
from .models import Userinfo
from django.http import HttpResponse
from django.http import HttpResponseRedirect
import json


def sign_in(request):
    stu_num = request.GET.get("stu_num")

    userinfo = Userinfo.objects.filter(stu_num=stu_num)
    if userinfo.count() != 0:
        request.session["stu_num"] = Userinfo.objects.filter(stu_num=stu_num)[0].stu_num
        request.session['username']=Userinfo.objects.filter(stu_num=stu_num)[0].username
    else:
        request.session["stu_num"] = ""
        request.session['username']=""

    return HttpResponseRedirect("/jwc/")


def sign_up(request):
    username = request.GET.get("username")
    college = request.GET.get("college")
    grade = request.GET.get("grade")
    stu_num = request.GET.get("stu_num")
    result = {}
    if not (stu_num and username and college and grade):
        result['context'] = "请完善信息再提交"
        return HttpResponse(json.dumps(result), content_type="application/json")

    if Userinfo.objects.filter(stu_num=stu_num).count() == 0:
        userinfo = Userinfo(username=username, college=college, grade=grade, stu_num=stu_num)
        userinfo.save()
        request.session["stu_num"] = stu_num
        request.session["username"]=username
        result['context'] = "欢迎，" + username
        return HttpResponse(json.dumps(result), content_type="application/json")

    else:
        result['context'] = "已经有人抢先一步注册啦"
        return HttpResponse(json.dumps(result), content_type="application/json")


def sign_out(request):
    request.session["username"] = ""
    request.session["stu_num"] = ""
    return HttpResponseRedirect("/jwc/")