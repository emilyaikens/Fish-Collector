from django.contrib import admin
from .models import Fish, Surveys, Collector

# Register your models here.
admin.site.register(Fish)
admin.site.register(Surveys)
admin.site.register(Collector)
