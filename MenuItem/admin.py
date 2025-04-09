from django.contrib import admin
from .models import MenuItem,Cart,Category,Order,OrderItem,Rating
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ['slug',]


admin.site.register(MenuItem)
admin.site.register(Cart)
admin.site.register(Category,PostAdmin)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Rating)