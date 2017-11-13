from __future__ import unicode_literals
 
from django.db import models
 
import re
import bcrypt

class CoursesManager(models.Manager):
    def course_validator(self, postData):
        error = {}
        if len(postData['name']) < 10:
            error['name'] = 'name must be longer than 10 characters'
        if len(postData['desc']) < 15:
            error['desc'] = 'description must be longer than 15 characters'
        return error

class Courses(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = CoursesManager()

