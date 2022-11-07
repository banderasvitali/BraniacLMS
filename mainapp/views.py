from django.views.generic import TemplateView
from datetime import datetime


class ContactsView(TemplateView):
    template_name = 'mainapp/contacts.html'
    
    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['contacts'] = [
            {
                'map': 'https://yandex.ru/map-widget/v1/-/CCUAZHcrhA',
                'city': 'Казань',
                'phone': '+7-999-22-22222',
                'email': 'geeklab@spb.ru',
                'address': 'Территория Петропавловская крепость, 3Ж',
            },{
                'map': 'https://yandex.ru/map-widget/v1/-/CCUAZHX3xB',
                'city': 'Санкт‑Петербург',
                'phone': '+7-999-11-11111',
                'email': 'geeklab@kz.ru',
                'address': 'Территория Кремль, 11, Казань, Республика Татарстан, Россия',
            },{
                'map': 'https://yandex.ru/map-widget/v1/-/CCUAZHh9kD',
                'city': 'Москва',
                'phone': '+7-999-33-33333',
                'email': 'geeklab@msk.ru',
                'address': 'Красная площадь, 7, Москва, Россия',
            },
        ]
        return context_data


class CoursesListView(TemplateView):
    template_name = 'mainapp/courses_list.html'


class DocSiteView(TemplateView):
    template_name = 'mainapp/doc_site.html'


class IndexView(TemplateView):
    template_name = 'mainapp/index.html'


class LoginView(TemplateView):
    template_name = 'mainapp/login.html'


class NewsView(TemplateView):
    template_name = 'mainapp/news.html'
    
    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['object_list'] = [
            {
                'title': 'Новость 1',
                'preview': 'Предварительное описание новости',
                'date': datetime.now()
            },{
                'title': 'Новость 2',
                'preview': 'Предварительное описание новости',
                'date': datetime.now()
            },{
                'title': 'Новость 3',
                'preview': 'Предварительное описание новости',
                'date': datetime.now()
            },{
                'title': 'Новость 4',
                'preview': 'Предварительное описание новости',
                'date': datetime.now()
            },{
                'title': 'Новость 5',
                'preview': 'Предварительное описание новости',
                'date': datetime.now()
            },
        ]
        return context_data
        
