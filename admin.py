from django.contrib import admin
from . models import oreg_tbl
from . models import renewal_tbl
from . models import emergency_tbl

# Register your models here.
admin.site.register(oreg_tbl)
admin.site.register(renewal_tbl)
admin.site.register(emergency_tbl)