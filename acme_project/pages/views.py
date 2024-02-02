from django.shortcuts import render
from birthday.models import Birthday


def homepage(request):
    staff = Birthday.objects.values(
        'first_name',
        'last_name',
        'birthday'
    )
    context = {'staff': staff}
    return render(request, 'pages/index.html', context)
