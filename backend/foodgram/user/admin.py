from django.contrib import admin
from .models import UserFoodgram


class UserFoodgramAdmin(admin.ModelAdmin):
    list_display = ('pk', 'username', 'first_name', 'last_name', 'email')
    list_filter = ('email', 'username')
    empty_value_display = '-пусто-'


admin.site.register(UserFoodgram, UserFoodgramAdmin)
