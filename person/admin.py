from django.contrib import admin
from .models import NewPerson, User, ContactsUser


class UserAdmin(admin.ModelAdmin):
    fields = ['username', 'phone'] # внутри каждого юзера будут показаны только эти поля
    list_display = ['id', 'username', 'email', 'phone', 'website', 'tags'] # показать поля в админке
    list_editable = ['username', 'phone', 'website', 'tags'] # редактировать поля в админке
    ordering = ['id'] #сортировка
    list_per_page = 3 # пагинация
    search_fields = ['username']
    list_filter = ['username', 'phone', 'website']
    # https: // www.youtube.com / watch?v = qMQkymZs3R8 & list = PLQAt0m1f9OHvGM7Y7jAQP8TKbBd3up4K2 & index = 57


admin.site.register(User, UserAdmin)

admin.site.register(NewPerson)
admin.site.register(ContactsUser)
