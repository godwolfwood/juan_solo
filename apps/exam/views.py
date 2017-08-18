from __future__ import unicode_literals
from django.shortcuts import render, redirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib import messages
import bcrypt
from .models import User

#GETS
def index(request):
    return render(request, "exam/index.html")

def success(request):
    context = {"name":User.objects.get(id=request.session["id"]).first_name}
    return render(request, "exam/success.html", context)

#POSTS
def register(request):
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
            user = User.objects.create(first_name = request.POST['first_name'],last_name = request.POST['last_name'],email = request.POST['email'],password=bcrypt.hashpw(request.POST['password'].encode(),bcrypt.gensalt()))
            request.session["id"] = user.id
            return redirect(reverse('login_success'))

def login(request):
    user = User.objects.filter(email=request.POST['email'])
    if len(user):
        if bcrypt.checkpw(request.POST['password'].encode(),user[0].password.encode()):
            request.session["id"] = user[0].id
            return redirect(reverse('login_success'))
        else:
            messages.error(request,"Failed to validate password!")
            return redirect(reverse('login_index'))
    else:
        messages.error(request,"Failed to find email in Database...")
        return redirect(reverse('login_index'))
