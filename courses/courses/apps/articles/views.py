from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render
from .models import Course, Comment
from django.urls import reverse

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

    search_courses_list = Course.objects.filter(course_title__startswith=what_search)

    return render(request, 'articles/search.html', {'search_courses_list': search_courses_list})

#тестовая страница
def test(request):
    return HttpResponse('This is test page!')