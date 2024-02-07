from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.urls import reverse

from .validators import real_age


class Birthday(models.Model):
    first_name = models.CharField(
        verbose_name='Имя',
        max_length=20,       
    )
    last_name = models.CharField(
        verbose_name='Фамилия',
        blank=True,
        help_text='Необязательное поле',
        max_length=20
    )
    birthday = models.DateField(
        verbose_name='Дата рождения',
        validators=(real_age,)
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
    email = models.EmailField(
        verbose_name='Электронная почта',
        max_length=30,
        default='example@contoso.com',
        unique=True
    )
    image = models.ImageField(
        verbose_name='Фото',
        upload_to='birthdays_images',
        blank=True
    )

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'
        constraints = (
            models.UniqueConstraint(
                fields=('first_name', 'last_name', 'birthday'),
                name='Unique person constraint',
            ),
        )

    
    def get_absolute_url(self):
        return reverse('birthday:detail', kwargs={'pk': self.pk})
    

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
