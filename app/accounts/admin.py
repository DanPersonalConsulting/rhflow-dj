from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User
from django.utils.translation import gettext_lazy as _

class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Informações Pessoais'), {'fields': ('name', 'username', 'avatar', 'funcionario')}),
        (_('Permissões'), {
            'fields': (
                'is_active', 
                'is_staff', 
                'is_superuser', 
                'is_hr_manager', 
                'is_org_admin', 
                'groups', 
                'user_permissions',
            )
        }),
        (_('Datas Importantes'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'name', 'username', 'password1', 'password2', 'is_active', 'is_staff', 'is_superuser', 'is_hr_manager', 'is_org_admin', 'groups'),
        }),
    )
    list_display = ('email', 'name', 'is_staff', 'is_hr_manager', 'is_org_admin', 'is_active', 'is_superuser')
    list_filter = ('is_staff', 'is_hr_manager', 'is_org_admin', 'is_active', 'groups')
    search_fields = ('email', 'name', 'username')
    ordering = ('email',)
    filter_horizontal = ('groups', 'user_permissions')
    readonly_fields = ('date_joined', 'last_login') 

admin.site.register(User, UserAdmin)
