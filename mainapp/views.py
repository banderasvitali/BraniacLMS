from django.views.generic import TemplateView


class ContactsView(TemplateView):
    template_name = 'mainapp/contacts.html'


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
                'date': '2022-11-07'
            },{
                'title': 'Новость 2',
                'preview': 'Предварительное описание новости',
                'date': '2022-11-07'
            },{
                'title': 'Новость 3',
                'preview': 'Предварительное описание новости',
                'date': '2022-11-07'
            },{
                'title': 'Новость 4',
                'preview': 'Предварительное описание новости',
                'date': '2022-11-07'
            },{
                'title': 'Новость 5',
                'preview': 'Предварительное описание новости',
                'date': '2022-11-07'
            },
        ]
        return context_data
        
