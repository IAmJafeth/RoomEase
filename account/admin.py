from django.contrib import admin
from .models import Account
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

class AccountInline(admin.StackedInline):
    model = Account
    can_delete = False
    verbose_name_plural = 'Accounts'

class CustomizedUserAdmin (UserAdmin):
    inlines = (AccountInline,)

class AccountAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone', 'active')
    list_filter = ('active',)
    search_fields = ('user', 'phone')


admin.site.unregister(User)
admin.site.register(User,CustomizedUserAdmin)
admin.site.register(Account, AccountAdmin)
