from django.contrib import admin
from .models import UserProfile, Papers

# Adding it to the admin panel
# Register your models here.
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('email', 'full_name')
    # list_display_links = ('email',)

class PapersAdmin(admin.ModelAdmin):
    list_display = ('paper_name', 'reviewed', 'file')
    list_editable = ('reviewed', )

admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Papers, PapersAdmin)