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
admin.site.register(Robo)