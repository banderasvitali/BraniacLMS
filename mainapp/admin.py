from django.contrib import admin

from mainapp.models import News

from mainapp.models import Courses

from mainapp.models import Lesson

from mainapp.models import CourseTeachers

admin.site.register(News)

admin.site.register(Courses)

admin.site.register(Lesson)

admin.site.register(CourseTeachers)