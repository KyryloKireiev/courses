from django.urls import path

from . import views

app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:course_id>/', views.detail, name='detail'),
    path('<int:course_id>/leave_comment/', views.leave_comment, name='leave_comment'),
    path('search_course/', views.search_course, name='search_course'),
    path('test/', views.test, name='test'),
]