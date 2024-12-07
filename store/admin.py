from django.contrib import admin

from.models import Product,Varieties

from store.models import User


# Register your models here.


admin.site.register(User)
admin.site.register(Varieties)
admin.site.register(Product)
