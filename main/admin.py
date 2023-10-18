from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Vendor)
admin.site.register(models.Product)
admin.site.register(models.ProductCategory)
admin.site.register(models.CustomerModel)
admin.site.register(models.OrderModel)
admin.site.register(models.OrderItemsModel)
admin.site.register(models.CustomerAddress)
admin.site.register(models.ProductRating)
admin.site.register(models.AddtoCarttt)
admin.site.register(models.Sizes)