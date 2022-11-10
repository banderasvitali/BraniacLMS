from django.db import models


class News(models.Model):
    title = models.CharField(max_length=256, verbose_name="Заголовок")
    preamble = models.CharField(max_length=1024, verbose_name="Вступление")
    
    body = models.TextField(blank=True, null=True, verbose_name="Содержимое")
    body_as_markdown = models.BooleanField(default=False, verbose_name="Разметка в формате Markdown")

    created = models.DateTimeField(auto_now_add=True, verbose_name="Создано")
    updated = models.DateTimeField(auto_now=True, verbose_name="Изменено")
    deleted = models.BooleanField(default=False, verbose_name="Удалено")

    def __str__(self):
        return f"{self.title}"

    def delete(self, *args, **kwargs):
        self.deleted = True
        self.save()



class Courses(models.Model):
    name = models.CharField(max_length=256, verbose_name="Название")
    description = models.TextField(verbose_name="Описание", blank=True, null=True)
    description_as_markdown = models.BooleanField(verbose_name="Разметка в формате Markdown", default=False)
    cost = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Стоимость", default=0)
    cover = models.CharField(max_length=25, default="no_image.svg", verbose_name="Лого курса")
    
    created = models.DateTimeField(auto_now_add=True, verbose_name="Создан")
    updated = models.DateTimeField(auto_now=True, verbose_name="Изменен")
    deleted = models.BooleanField(default=False, verbose_name="Удален")
    
    def __str__(self):
        return f"{self.title}"

    def delete(self, *args, **kwargs):
        self.deleted = True
        self.save()



class Lesson(models.Model):
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    num = models.PositiveIntegerField(verbose_name="Номер урока")
    title = models.CharField(max_length=256, verbose_name="Тема урока")
    description = models.TextField(verbose_name="Описание", blank=True, null=True)
    description_as_markdown = models.BooleanField(verbose_name="Разметка в формате Markdown", default=False)
    
    created = models.DateTimeField(auto_now_add=True, verbose_name="Создан", editable=False)
    updated = models.DateTimeField(auto_now=True, verbose_name="Изменен", editable=False)
    deleted = models.BooleanField(default=False, verbose_name="Удален")
    
    def __str__(self):
        return f"{self.title}"

    def delete(self, *args, **kwargs):
        self.deleted = True
        self.save()
    
     
class CourseTeachers(models.Model):
    course = models.ManyToManyField(Courses)
    name_first = models.CharField(max_length=128, verbose_name="Имя")
    name_second = models.CharField(max_length=128, verbose_name="Фамилия")
    day_birth = models.DateField(verbose_name="Дата рождения")
    deleted = models.BooleanField(default=False, verbose_name="Удален")
    
    def __str__(self) -> str:
        return "{0:0>3} {1} {2}".format(self.pk, self.name_second, self.name_first)
    
    def delete(self, *args, **kwargs):
        self.deleted = True
        self.save()

