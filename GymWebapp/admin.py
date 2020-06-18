from django.contrib import admin
from .models import Packages,Subscription,Customer_Details,Workoutplan


admin.site.register(Packages)
admin.site.register(Subscription)
admin.site.register(Customer_Details)
admin.site.register(Workoutplan)
