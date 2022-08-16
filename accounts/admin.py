from django.contrib import admin
from main.models import User, Article


@admin.register(User)
@admin.register(Article)
class UserAdmin(admin.ModelAdmin):
    readonly_fields = ['id']
    pass
