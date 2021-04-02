from info.models import Tickets
from django.contrib import admin
from .models import Trains
from info.models import Avail, Tickets
# Register your models here.

admin.site.register(Trains)
admin.site.register(Tickets)
admin.site.register(Avail)