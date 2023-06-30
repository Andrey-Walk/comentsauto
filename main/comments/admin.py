from django.contrib import admin
from .models import Countrys
from .models import Directors
from .models import Cars
from .models import Comments

admin.site.register(Countrys)
admin.site.register(Directors)
admin.site.register(Cars)
admin.site.register(Comments)