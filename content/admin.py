from django.contrib import admin

from .models import Course, Video, Pricing, Subscription

admin.site.site_header = "Country Livers Institute Admin"
admin.site.site_title = "Country Livers Institute Admin Portal"
admin.site.index_title = "Welcome to the Country Livers Institute Admin Portal"
admin.site.register(Course)
admin.site.register(Video)
admin.site.register(Pricing)
admin.site.register(Subscription)
