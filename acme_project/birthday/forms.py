from django import forms
from django.core.exceptions import ValidationError
# импортируем класс модели Birthday для создания формы по образу модели
from .models import Birthday
from .validators import real_age
'''Создадим новый класс на основе модели из БД. Старый класс закомментируем'''

# Множество с именами участников Ливерпульской четвёрки.
BEATLES = {'Джон Леннон', 'Пол Маккартни', 'Джордж Харрисон', 'Ринго Старр'}


class BirthdayForm(forms.ModelForm):
    # Все настройки задаём в подклассе Meta.
    class Meta:
        # Указываем модель, на основе которой должна строиться форма.
        model = Birthday
        # Указываем, что надо отобразить все поля.
        fields = '__all__'
        # Виджеты с календариком для поля дата рождения и поля описание указываем как и было
        widgets = {
            'birthday': forms.DateInput(attrs={'type': 'date'}),
            'description': forms.Textarea(attrs={'cols': '20', 'rows': '5'}),
            'salary': forms.NumberInput(attrs={'max': '100000', 'min': '10000'})
        }


    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        return first_name.split()[0]
        

    def clean(self):
            # наследуем метод из родительского класса (constraints из файла models.py)
            super().clean()
            # Получаем имя и фамилию из очищенных полей формы.
            first_name = self.cleaned_data['first_name']
            last_name = self.cleaned_data['last_name']
            # Проверяем вхождение сочетания имени и фамилии во множество имён.
            if f'{first_name} {last_name}' in BEATLES:
                raise ValidationError(
                    'Мы тоже любим Битлз, но введите, пожалуйста, настоящее имя!'
                )


''' старый класс, оставляю для образца
class BirthdayForm(forms.Form):
    first_name = forms.CharField(
        label='Имя',
        max_length=20
    )
    last_name = forms.CharField(
        label='Фамилия',
        required=False,
        help_text='Необязательное поле'
    )
    birthday = forms.DateField(
        label='Дата рождения',
        widget=forms.DateInput(attrs={'type': 'date'}),
        validators=(real_age,),
    )
    """Добавил поля формы для тестов задания из тренажёра
    description = forms.CharField(
        label='Описание',
        required=False,
        widget=forms.Textarea(attrs={'cols': '20', 'rows': '5'}) - многострочный текст, окно 20 х 5
    )
    price = forms.IntegerField(
        label='Цена',
        help_text='Рекомендованная розничная цена',
        min_value=10,
        max_value=100,
        #widget=forms.NumberInput(attrs={'max': '100', 'min': '10'}),
        #initial=10 - значение поля по умолчанию
    )"""
'''
