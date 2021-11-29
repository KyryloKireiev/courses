from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render
from .models import Course, Comment
from django.urls import reverse
from django.utils import timezone
import datetime

#отображение списка курсов

def index(request):
    latest_courses_list = Course.objects.order_by('pub_date')
    return render(request, 'articles/list.html', {'latest_courses_list': latest_courses_list})
#детали курса
def detail(request, course_id):
    try:
        a = Course.objects.get(id=course_id)
    except:
        raise Http404('Курс не найден!')

    latest_comment_list = a.comment_set.order_by('-id')[:5]

    return render(request, 'articles/detail.html', {'course': a, 'latest_comment_list': latest_comment_list})
#комментарии
def leave_comment(request, course_id):
    try:
        a = Course.objects.get(id=course_id)
    except:
        raise Http404('Комментарии не найдены!')

    a.comment_set.create(author_name=request.POST['name'], comment_text=request.POST['text'])

    return HttpResponseRedirect(reverse('articles:detail', args=(a.id,)))
#поиск по названию курса
def search_course(request):
    if 'what_search' in request.GET and request.GET['what_search']:
        what_search = request.GET['what_search']

    #search_courses_list = Course.objects.filter(course_title__startswith=what_search)
    search_courses_list = Course.objects.filter(course_title__contains=what_search)

    return render(request, 'articles/search.html', {'search_courses_list': search_courses_list})

#фильтр курсов по дате добавления
def date_filter(request):
    if 'begin_year' in request.GET and request.GET['begin_year']:
        begin_year = request.GET['begin_year']
    if 'begin_month' in request.GET and request.GET['begin_month']:
        begin_month = request.GET['begin_month']
    if 'begin_day' in request.GET and request.GET['begin_day']:
        begin_day = request.GET['begin_day']

    if 'end_year' in request.GET and request.GET['end_year']:
        end_year = request.GET['end_year']
    if 'end_month' in request.GET and request.GET['end_month']:
        end_month = request.GET['end_month']
    if 'end_day' in request.GET and request.GET['end_day']:
        end_day = request.GET['end_day']


        begin_search = begin_year + begin_month + begin_day
        end_search = end_year + end_month + end_day

        start = datetime.datetime.strptime(begin_search, '%Y%m%d')
        new_end = datetime.datetime.strptime(end_search, '%Y%m%d')
    a = Course.objects.filter(pub_date__range=[start, new_end])

    return render(request, 'articles/date_filter.html', {'a': a})


#тестовая страница
def test(request):
    return HttpResponse('This is test page!')