from django.contrib import admin
from .models import User, Category, Transaction, Setting, Analytics, DragonState

admin.site.register(User)
admin.site.register(Category)
admin.site.register(Transaction)
admin.site.register(Setting)
admin.site.register(Analytics)
admin.site.register(DragonState)
