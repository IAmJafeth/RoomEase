from django.contrib import admin
from .models import TwilioAccount

class TwilioAccountAdmin(admin.ModelAdmin):
    list_display = ('account_sid', 'auth_token', 'phone_number', 'active')
    list_filter = ('active',)
    search_fields = ('account_sid', 'phone_number')
    ordering = ['account_sid']

admin.site.register(TwilioAccount, TwilioAccountAdmin)
