# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import re


# Create your models here.
class UserManager(models.Manager):
    def validator(self,postData):
        errors = {}
        if len(postData["name"]) < 2:
            errors["name"] = "Name should be more than 3 characters"
        if len(postData["username"]) < 2:
            errors["username"] = "Name should be more than 3 characters"
        if len(postData["password"]) < 8:
            errors["password"] = "Password should be more than 8 characters"
        if postData["password"] != postData["confirm"]:
            errors["confirm"] = "Passwords don't match"
        if len(postData["date_hired"]) < 1:
            errors["date_hired"] = "Date hired cant be empty"
        return errors;

class User(models.Model):
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    hired_at = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()
    def __repr__(self):
        return "<User object: name = {} email = {} hired_at = {}>".format(self.name, self.email,self.hired_at)

class WishManager(models.Manager):
    def validator(self,postData):
        errors = {}
        if len(postData["name"]) < 1:
            errors["name"] = "Name should be more than 2 characters"
        return errors;
    
class Wish(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User, related_name = "wish_list")
    wish_by = models.ManyToManyField(User, related_name = "liked_list")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = WishManager()
    def __repr__(self):
        return "<Wish object: name = {}>".format(self.name)
