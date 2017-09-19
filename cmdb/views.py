# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

# Create your views here.
from django.shortcuts import HttpResponse
from django.shortcuts import render


def login(request):
    err_msg = ''
    if request.method == "POST":
        username = request.POST.get("user", None)
        pwd = request.POST.get("pwd", None)
        if username == "root" and pwd == "123":
            return redirect("/home")
        else:
            err_msg = "用户名或者密码错误！"
    return render(request, "login.html", {"error_msg": err_msg})
userlist=[]
for i in range(10):
    userlist.append({"username":"zs"+str(i),"gender":"male","age":"18"})



def home(request):
    if request.method=="POST":
        user=request.POST.get("user",None)
        gd=request.POST.get("gd",None)
        age = request.POST.get("age", None)#getlist()获取一个列表用于checkbox
        if user and gd and age:
            temp={"username":user,"gender":gd,"age":age}
            userlist.append(temp)
    return render(request,"home.html",{"user_list":userlist})
