from datetime import date

from django.shortcuts import render
from django.views.generic import TemplateView

from birthday.models import Birthday

class HomePage(TemplateView):
    template_name = 'pages/index.html'

    def get_context_data(self, **kwargs):
        # Получаем словарь контекста из родительского метода.
        context = super().get_context_data(**kwargs)
        # Добавляем в словарь ключ total_count;
        # значение ключа — число объектов модели Birthday.
        context['staff'] = Birthday.objects.values(
            'first_name',
            'last_name',
            'email',
        ).order_by('id')[:5]
        context['total_count'] = Birthday.objects.count()
        # Возвращаем изменённый словарь контекста.
        return context

'''Переезжаем на класс HomePage'''
def homepage(request):
    staff = Birthday.objects.values(
        'first_name',
        'last_name',
        'email'
    ).filter(
        birthday=date.today() # Доделать. сейчас возвращает только тех, у кого день рождения именно сегодня, в этот год
    ).order_by(
        'id'
    )[:5]
    context = {'staff': staff}
    return render(request, 'pages/index.html', context)
