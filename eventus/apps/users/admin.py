from django.contrib import admin
from .models import User
from import_export import resources
from .actions import ExportCsvMixin
@admin.register(User)
class UserAdmin(admin.ModelAdmin, ExportCsvMixin):
    list_display = ('username', 'first_name', 'last_name','email')
    search_fields = ('username','email')
    list_filter = ('is_superuser',)
    ordering= ('username',)
    actions = ['export_as_csv']
    filter_horizontal = ('groups','user_permissions')
    
    fieldsets = (
        ('User',{'fields':('username','password')}),
        ('Personal Info',{'fields':(  'first_name',
                                    'last_name',
                                    'email',
                                    'photo',    
                                )}),
         ('Permissions',{'fields':( 'is_active',
                                    'is_staff',
                                    'is_superuser',
                                    'groups',
                                    'user_permissions',
                                )}),
    )

    
    #def admin_action(self, request,queryset):





