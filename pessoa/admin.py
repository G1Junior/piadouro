from django.contrib import admin
from pessoa.models import Perfil
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
class perfilInline(admin.StackedInline):
    model = Perfil
    can_delete = False
    verbose_name_plural = 'perfil'

class UserAdmin(BaseUserAdmin):
    inlines = (perfilInline,)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)