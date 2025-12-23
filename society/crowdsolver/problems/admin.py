from django.contrib import admin
from .models import signup, Category, raiseproblem, givesuggestion,voting

# Register your models here.
admin.site.register(signup)
admin.site.register(Category)
admin.site.register(raiseproblem)
admin.site.register(givesuggestion)
admin.site.register(voting)