from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from time import strftime, localtime
from django.core.urlresolvers import reverse
 
from models import *

def index(request):
    courses = Courses.objects.all()
    context = {
        'courses': courses    
    }
    return render(request, 'courses_app/index.html', context)

def add_course(request):
    error = Courses.objects.course_validator(request.POST)
    if len(error):
        for tag, error in error.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/')
    else:
        Courses.objects.create(name=request.POST['name'], desc=request.POST['desc'])
        return redirect('/')

def delete(request, course_id):
    course = Courses.objects.get(id=course_id)
    course.delete()
    return redirect('/')