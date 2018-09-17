from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from human.forms import UserCreationForm, UserChangeForm

UserModel = get_user_model()

class UserAdmin(BaseUserAdmin):
    model = UserModel
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('username', 'first_name', 'last_name', 'contact', 'email', 'is_staff')

    fieldsets = BaseUserAdmin.fieldsets
    fieldsets[1][1]['fields'] += ('contact', )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'contact', 'password1', 'password2')}
        ),
    )
    

admin.site.register(UserModel, UserAdmin)
