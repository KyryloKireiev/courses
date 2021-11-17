import datetime
from django.db import models
from django.utils import timezone

class Course(models.Model):
    course_title = models.CharField('Название курса:', max_length=250)
    course_text = models.TextField('Краткое описание курса:', max_length=500)
    pub_date = models.DateTimeField('Дата публикации курса:')

    def __str__(self):
        return self.course_title

    def was_published_resently(self):
        return self.pub_date >= (timezone.now() - datetime.timedelta(days=30))

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'

class Comment(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    author_name = models.CharField('Автор коментария:', max_length=50)
    comment_text = models.TextField('Текст комментария:', max_length=500)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'


