from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Birthday(models.Model):
    first_name = models.CharField(
        verbose_name='Имя',
        max_length=20
    )
    last_name = models.CharField(
        verbose_name='Фамилия',
        blank=True,
        help_text='Необязательное поле',
        max_length=20
    )
    birthday = models.DateField(
        verbose_name='Дата рождения'
    )
    description = models.TextField(
        verbose_name='Описание',
        blank=True,
        help_text='пара слов о сотруднике',
    )
    salary = models.IntegerField(
        verbose_name='Зарплата (руб)',
        default='0',
        validators = [MinValueValidator(10000), MaxValueValidator(100000)]
    )
