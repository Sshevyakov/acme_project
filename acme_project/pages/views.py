from django.shortcuts import render
from datetime import date
from birthday.models import Birthday


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
