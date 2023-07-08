from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Login

# Register your models here.

class UserAdmin(BaseUserAdmin):
    
    actions = ['toggle_staff_status', 'delete_selected_custom']

    def toggle_staff_status(self, request, queryset):
        for user in queryset:
            user.is_staff = not user.is_staff
            user.save()
        
    toggle_staff_status.short_description = "Turn staff status on/off"

    def delete_selected_custom(self, request, queryset):
        queryset.delete()

    delete_selected_custom.short_description = "Delete selected users"

    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

admin.site.unregister(User)
admin.site.register(User, UserAdmin)


admin.site.site_header = "Home"
admin.site.index_title = "Simple Login page created by Rauf Mekhraliev"

@admin.register(Login)
class LoginAdmin(admin.ModelAdmin):
    list_display = ('email', 'password')
    search_fields = ('email',)
    