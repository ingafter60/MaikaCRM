from django.contrib import admin

# Register your models here.

# from .models import Customer
# from .models import Product
# from .models import Order
from .models import * # equal to line 5 to 7

admin.site.register(Customer)
admin.site.register(Tag)
admin.site.register(Product)
admin.site.register(Order)