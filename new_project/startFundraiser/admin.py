from django.contrib import admin

# Register your models here.

from .models import Campaign, FAQs

admin.site.register(Campaign)
admin.site.register(FAQs)
