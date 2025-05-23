from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Profile
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
# Register your models here.

# class UserCreationForm(forms.ModelForm):
#     password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
#     password2 = forms.CharField(label='Password confirmation')
    
# class CustomUserCreationForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields=('email',)
        

class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('email','is_superuser','is_active')
    list_filter = ('email','is_superuser','is_active')
    searching_fields = ('email',)
    ordering = ('email',)
    fieldsets = (
        ('Authentication', {
            "fields": (
                'email', 'password'
            ),
        }),
        ('permissions', {
            "fields": (
                'is_active', 'is_staff', 'is_superuser'
            ),
        }),

        ('group permissions', {
            "fields": (
                'groups', 'user_permissions'
            ),
        }),
        ('important date', {
            "fields": (
                'last_login',
            ),
        }),
    )
    
    
    add_fieldsets = (
        (None, {
            'classes':('wide',),
            'fields':('email', 'password1','password2', 'is_staff', 'is_active','is_superuser')
        }),
    )
admin.site.register(Profile) 
admin.site.register(User,CustomUserAdmin)