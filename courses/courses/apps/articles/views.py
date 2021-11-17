from django.http import HttpResponse
from django.shortcuts import render
from .models import Course, Comment

def index(request):
    latest_courses_list = Course.objects.order_by('-pub_date')[:5]
    return render(request, 'articles/list.html', {'latest_courses_list' : latest_courses_list})

def detail(request, course_id):
    pass


def test(request):
    return HttpResponse('This is test page!')