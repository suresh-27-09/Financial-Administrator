from django.contrib import admin

from .models import Register,customer,Products,Cart,CartDetails

admin.site.register(Register)
admin.site.register(customer)
admin.site.register(Products)
admin.site.register(Cart)
admin.site.register(CartDetails)
