# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'^[a-zA-Z]{2,}$')
PASSWORD_REGEX = re.compile(r'^.{8,}$')

# Create your models here.
class UserManager(models.Manager):
    def validator(self,postData):
        errors = {}
        if not NAME_REGEX.match(postData["last_name"]):
            errors["first_name"] = "First name should be more than 2 characters and only letters"
        if not NAME_REGEX.match(postData["last_name"]):
            errors["last_name"] = "Last name should be more than 2 characters and only letters"
        if not EMAIL_REGEX.match(postData["email"]):
            errors["email"] = "Entered an invalid email" 
        if len(postData["password"]) < 8:
            errors["password"] = "Password should be more than 8 characters"
        if postData["password"] != postData["confirm"]:
            errors["confirm"] = "Passwords don't match"
        return errors;

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()