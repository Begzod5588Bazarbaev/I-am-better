from django.contrib import admin
from .models import *
from .forms import *
from django.contrib.auth.admin import UserAdmin

@admin.register(User)
class CustomUserAdmin(UserAdmin):
	add_form = CustomUserCreationForm
	form = CustomUserChangeForm
	model = User
	list_display = ['email','username','name','is_staff',]
	list_display_links = ['username',]
	fieldsets = UserAdmin.fieldsets + ((None,{'fields':('name',)}),)
	add_fieldsets = UserAdmin.fieldsets + ((None,{'fields':('name',)}),)

admin.site.register(Calendar)
admin.site.register(Invites)
admin.site.register(Event)
