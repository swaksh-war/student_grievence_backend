from django.contrib import admin
from .models import Event, Complaint, CustomUser
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'password', 'phone_number', 'department', 'year', 'user_type', 'unique_id')

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = CustomUser
        fields = ('username', 'password', 'phone_number', 'department', 'year', 'user_type', 'unique_id')


class CustomUserAdmin(BaseUserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['username', 'email', 'phone_number', 'department', 'year', 'user_type', 'unique_id', 'is_staff']
    fieldsets = BaseUserAdmin.fieldsets + (
        (None, {'fields': ('phone_number', 'department', 'year', 'user_type', 'unique_id')}),
    )
    add_fieldsets = BaseUserAdmin.add_fieldsets + (
        (None, {'fields': ('username', 'email', 'password1', 'password2', 'phone_number', 'department', 'year', 'user_type', 'unique_id')}),
    )
    


# Register your models here.
admin.site.register(Event)
admin.site.register(Complaint)
admin.site.register(CustomUser)