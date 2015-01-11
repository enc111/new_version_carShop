from django.contrib import admin
from Car.models import Car, Dealer, Model, Mark, Comments
from checkup.models import Checkup, TypeOfService
from testdrive.models import Testdrive
from order.models import Order

# Register your models here.


class CarCom(admin.StackedInline):
    model = Comments
    extra = 1


class CarAdmin(admin.ModelAdmin):
    inlines = [CarCom]


admin.site.register(Car, CarAdmin)
admin.site.register(Dealer)
admin.site.register(Model)
admin.site.register(Mark)
admin.site.register(Comments)
admin.site.register(Checkup)
admin.site.register(TypeOfService)
admin.site.register(Testdrive)
admin.site.register(Order)
