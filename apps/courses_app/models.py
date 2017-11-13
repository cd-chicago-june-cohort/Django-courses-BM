from __future__ import unicode_literals
 
from django.db import models
 
import re
import bcrypt

class CoursesManager(models.Manager):
    def course_validator(self, postData):
        errors = {}
        if len(postData['name']) < 10:
            errors['name'] = 'name must be longer than 10 characters'
        if len(postData['description']) < 15:
            errors['desc'] = 'description must be longer than 15 characters'
        return errors

class Courses(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = CoursesManager()

