from __future__ import unicode_literals
from django.shortcuts import render, redirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib import messages
import bcrypt
from .models import *

#GETS
def index(request):
    return render(request, "exam/index.html")

def success(request):
    user = User.objects.get(id=request.session["id"])
    context = {
        "user": user,
        "list": user.liked_list.all(),
        "all_wish": Wish.objects.exclude(user = user),
    }
    return render(request, "exam/dashboard.html", context)

def add(request):
    return render(request, "exam/new.html")

def show(request,number):
    wish = Wish.objects.get(id=number)
    context = {
        "wish": wish,
        "list": wish.wish_by.all(),
    }
    return render(request, "exam/show.html", context)
def delete(request,number):
    Wish.objects.get(id=number).delete()
    return redirect(reverse('login_success'))
def remove(request,number):
    User.objects.get(id=request.session["id"]).liked_list.remove(Wish.objects.get(id=number))
    return redirect(reverse('login_success'))
def wish_add(request,number):
    User.objects.get(id=request.session["id"]).liked_list.add(Wish.objects.get(id=number))
    return redirect(reverse('login_success'))
#POSTS
def register(request):
    if request.method == "POST":
        errors = User.objects.validator(request.POST)
        if len(errors):
            for tag, error in errors.iteritems():
                messages.error(request,error, extra_tags=tag)
            return redirect(reverse('login_index'))
        else:
            users = User.objects.filter(email=request.POST['email'])
            if len(users):
                messages.error(request,"This email is already in use!")
                return redirect(reverse('login_index'))
            else:
                user = User.objects.create(name = request.POST['name'],username = request.POST['username'],email = request.POST['email'],password=bcrypt.hashpw(request.POST['password'].encode(),bcrypt.gensalt()),hired_at = request.POST['date_hired'])
                request.session["id"] = user.id
                return redirect(reverse('login_success'))
    else:
        return redirect(reverse('login_index'))
def login(request):
    if request.method == "POST":
        user = User.objects.filter(username=request.POST['name'])
        if len(user):
            if bcrypt.checkpw(request.POST['password'].encode(),user[0].password.encode()):
                request.session["id"] = user[0].id
                return redirect(reverse('login_success'))
            else:
                messages.error(request,"Failed to validate password!")
                return redirect(reverse('login_index'))
        else:
            messages.error(request,"Failed to find Username in Database...")
            return redirect(reverse('login_index'))
    else:
        return redirect(reverse('login_index'))

def create(request):
    if request.method == "POST":
        errors = Wish.objects.validator(request.POST)
        if len(errors):
            for tag, error in errors.iteritems():
                messages.error(request,error, extra_tags=tag)
            return redirect(reverse('login_add'))
        wish = Wish.objects.create(name = request.POST['name'], user = User.objects.get(id=request.session["id"]))
        wish.wish_by.add(User.objects.get(id=request.session["id"]))
        return redirect(reverse('login_success'))
    else:
        return redirect(reverse('login_index'))