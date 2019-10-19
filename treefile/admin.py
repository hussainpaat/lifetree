from django.contrib import admin
from . models import category, service, gallery, blog, doctor, testimonial

admin.site.register(category)
admin.site.register(service)
admin.site.register(gallery)
admin.site.register(blog)
admin.site.register(doctor)
admin.site.register(testimonial)