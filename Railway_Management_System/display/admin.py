from info.models import Tickets
from django.contrib import admin
from .models import Trains
# Register your models here.

admin.site.register(Trains)
admin.site.register(Tickets)