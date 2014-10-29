from django.contrib import admin
from hr_app.models import Organization, Honoree, Honor
from mptt.admin import MPTTModelAdmin

admin.site.register(Honoree)
admin.site.register(Honor)
admin.site.register(Organization)