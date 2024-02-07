from django.contrib import admin

from .models import Birthday


class BirthdayAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'birthday',
        'email',
    )
    list_editable = (
        'birthday',
        'email',
    )

admin.site.register(Birthday, BirthdayAdmin)
