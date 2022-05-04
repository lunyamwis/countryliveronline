from django.contrib import admin

from .models import Course, Pricing, Subscription, Video

admin.site.site_header = (
    "Country Livers Manual And Domestic Labor Training Institute Admin"
)
admin.site.site_title = (
    "Country Livers Manual And Domestic Labor Training Institute Admin Portal"
)
admin.site.index_title = "Welcome to the Country Livers Manual And \
Domestic Labor Training Institute Admin Portal"
admin.site.register(Course)
admin.site.register(Video)
admin.site.register(Pricing)
admin.site.register(Subscription)
