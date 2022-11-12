from django.contrib import admin

from .models import Recipient, Reason, Present, Date, RemindForDays, AboutPresent

admin.site.register(Recipient)
admin.site.register(Reason)
admin.site.register(Present)
admin.site.register(Date)
admin.site.register(RemindForDays)
admin.site.register(AboutPresent)

# Register your models here.
