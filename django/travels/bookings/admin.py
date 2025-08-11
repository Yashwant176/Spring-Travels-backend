from django.contrib import admin
from .models import Bus,Seat
# Register your models here.
class BusAdmin(admin.ModelAdmin):
    list_display=('bus_name','number','origin','destination')
admin.site.register(Bus,BusAdmin)
admin.site.register(Seat)