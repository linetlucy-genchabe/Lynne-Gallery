from django.contrib import admin
from .models import Editor, Pictures,Location,Category

# Register your models here.

admin.site.register(Editor)
admin.site.register(Pictures)
admin.site.register(Location)
admin.site.register(Category)


