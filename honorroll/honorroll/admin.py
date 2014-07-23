from django.contrib import admin
from .models import Honor, Organization, Honoree

# Register your models here.

admin.site.register(Organization)
admin.site.register(Honoree)
admin.site.register(Honor)