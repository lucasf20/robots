from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Cliente, Robo, Usuario

# Register your models here.
class MyUserAdmin(UserAdmin):

    fieldsets = (
        (None, {
            'classes':('wide',),
            'fields':('username', 'password','first_name',
             'last_name', 'email', 'cliente', 'groups', 'user_permissions', 'is_staff', 'is_superuser')
        }),
    )    

    add_fieldsets = (
        (None, {
            'classes':('wide',),
            'fields':('username', 'password1', 'password2', 'first_name', 'last_name', 'email', 'cliente','is_staff')
        }),
    )

admin.site.register(Usuario, MyUserAdmin)
admin.site.register(Cliente)

class RoboAdmin(admin.ModelAdmin):
    ordering = ('codigo',)
    search_fields = ('codigo','cliente__nome_da_empresa','campo1','campo2','campo3')
    list_display= ('codigo', 'cliente', 'campo1','campo2','campo3')

admin.site.register(Robo, RoboAdmin)