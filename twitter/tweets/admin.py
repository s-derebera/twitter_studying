from django.contrib import admin
from django.contrib.auth.models import Group, User
from .models import Profile
#Unregister Groups

admin.site.unregister(Group)
# Mix Profile info into User one
class ProfileInline(admin.StackedInline):
    model = Profile
    
class UserAdmin(admin.ModelAdmin):
    model = User
    # Just display username fields on admin page
    fields = ["username"]
    inlines = [ProfileInline]

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
# admin.site.register(Profile)

