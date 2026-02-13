from django.contrib import admin
from .models import Location, Supplier, Person, Asset, Task
admin.site.register(Location)
admin.site.register(Supplier)
admin.site.register(Person)
admin.site.register(Asset)
admin.site.register(Task)
