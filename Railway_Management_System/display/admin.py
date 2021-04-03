from django.contrib import admin
from .models import Trains
from info.models import Avail, Tickets
from feedback.models import Feedback

# Register your models here.

admin.site.register(Trains)
admin.site.register(Tickets)
admin.site.register(Avail)
admin.site.register(Feedback)