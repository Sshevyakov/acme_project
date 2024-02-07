from django.shortcuts import get_object_or_404, redirect, render
from django.core.paginator import Paginator
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from django.urls import reverse_lazy

from .forms import BirthdayForm
from .models import Birthday
from .utils import calculate_birthday_countdown


'''Эта функция более не нужна (НУЖНА), так как теперь по пути "birthday/" вызывается метод класса BirthdayCreateView (см CBV)'''
# def birthday(request, pk=None):
#     # Если в запросе указан pk (если получен запрос на редактирование объекта):
#     if pk is not None:
#         # Получаем объект модели или выбрасываем 404 ошибку.
#         instance = get_object_or_404(Birthday, pk=pk)
#     # Если в запросе не указан pk
#     # (если получен запрос к странице создания записи):
#     else:
#         # Связывать форму с объектом не нужно, установим значение None.
#         instance = None
#     # Передаём в форму либо данные из запроса, либо None. 
#     # В случае редактирования прикрепляем объект модели.
#     form = BirthdayForm(
#         request.POST or None,
#         files=request.FILES or None,
#         instance=instance
#     )
#     context = {'form': form}
#     if form.is_valid():
#         form.save()
#         birthday_countdown = calculate_birthday_countdown(
#             form.cleaned_data['birthday']
#         )
#         context.update({'birthday_countdown': birthday_countdown})
#         #При редактировании данные сохраняются и пользователь попадает на страницу со всеми сотрудниками
#         return redirect('birthday:list')
#     return render(request, 'birthday/birthday.html', context)


class BirthdayMixin:
    model = Birthday
    success_url = reverse_lazy('birthday:list')


class BirthdayFormMixin:
    form_class = BirthdayForm
    template_name = 'birthday/birthday.html'


class BirthdayCreateView(BirthdayMixin, BirthdayFormMixin, CreateView):
    pass
    # Не нужно описывать атрибуты: все они унаследованы от BirthdayMixin(Все что написано ниже осталось от самостоятельного класса)
    # # Указываем модель, с которой работает CBV
    # model = Birthday
    # # Этот класс сам может создать форму на основе модели!
    # # Нет необходимости отдельно создавать форму через ModelForm.
    # # Указываем поля, которые должны быть в форме: (Отредактировали: теперь забираем виджеты из формы)
    # form_class = BirthdayForm
    # # Явным образом указываем шаблон: (Так как шаблон по умолчанию должке быть "birthday_form.html.")
    # template_name = 'birthday/birthday.html'
    # # Указываем namespace:name страницы, куда будет перенаправлен пользователь
    # # после создания объекта:
    # success_url = reverse_lazy('birthday:list')


class BirthdayUpdateView(BirthdayMixin, BirthdayFormMixin, UpdateView):
    pass
    # model = Birthday
    # form_class = BirthdayForm
    # template_name = 'birthday/birthday.html'
    # success_url = reverse_lazy('birthday:list')

'''Так же меняем на CBV'''
# def delete_birthday(request, pk):
#     # Получаем объект модели или выбрасываем 404 ошибку.
#     instance = get_object_or_404(Birthday, pk=pk)
#     # В форму передаём только объект модели;
#     # передавать в форму параметры запроса не нужно.
#     form = BirthdayForm(instance=instance)
#     context = {'form': form}
#     # Если был получен POST-запрос...
#     if request.method == 'POST':
#         # ...удаляем объект:
#         instance.delete()
#         # ...и переадресовываем пользователя на страницу со списком записей.
#         return redirect('birthday:list')
#     # Если был получен GET-запрос — отображаем форму.
#     return render(request, 'birthday/birthday.html', context)


class BirthdayDeleteView(BirthdayMixin, DeleteView):
    pass


'''Эта функция более не нужна, так как теперь по пути "birthday/list/" вызывается метод класса BirthdayListView (см CBV)'''
# def birthday_list(request):
#     birthdays = Birthday.objects.order_by(
#         'id'
#     )
#     # Создаём объект пагинатора с количеством 10 записей на страницу.
#     paginator = Paginator(birthdays, 3)

#     # Получаем из запроса значение параметра page.
#     page_number = request.GET.get('page')
#     # Получаем запрошенную страницу пагинатора. 
#     # Если параметра page нет в запросе или его значение не приводится к числу,
#     # вернётся первая страница.
#     page_obj = paginator.get_page(page_number)
#     # Вместо полного списка объектов передаём в контекст 
#     # объект страницы пагинатора
#     context = {'page_obj': page_obj}
#     return render(request, 'birthday/birthday_list.html', context)


# Наследуем класс от встроенного ListView:
class BirthdayListView(ListView):
    # Указываем модель, с которой работает CBV...
    model = Birthday
    # ...сортировку, которая будет применена при выводе списка объектов:
    ordering = 'id'
    # ...и даже настройки пагинации:
    paginate_by = 3