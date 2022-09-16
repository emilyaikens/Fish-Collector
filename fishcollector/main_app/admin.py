from django.contrib import admin
from .models import Fish, Surveys

# Register your models here.
admin.site.register(Fish)
admin.site.register(Surveys)

##register Toy equivalent here, and add to import at top (line 2)