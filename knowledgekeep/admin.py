from django.contrib import admin
from .models import UserProfile #, Papers

# Adding it to the admin panel
# Register your models here.
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('email', 'full_name')
    # list_display_links = ('email',)

admin.site.register(UserProfile, UserProfileAdmin)
# admin.site.register(Papers)