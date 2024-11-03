from django.contrib import admin
from .models import (
    YourModel1,
    YourModel2,
    YourModel3
)  # Import your models here

# Define custom admin classes for better control over the admin interface

class YourModel1Admin(admin.ModelAdmin):
    list_display = ('field1', 'field2', 'field3')  # Fields to display in the list view
    search_fields = ('field1', 'field2')  # Fields to be searchable
    list_filter = ('field3',)  # Fields to filter by in the admin

class YourModel2Admin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'is_active')
    search_fields = ('name',)
    list_filter = ('is_active',)

class YourModel3Admin(admin.ModelAdmin):
    list_display = ('title', 'updated_at')
    search_fields = ('title',)
    list_filter = ('status',)

# Register your models with the admin site
admin.site.register(YourModel1, YourModel1Admin)
admin.site.register(YourModel2, YourModel2Admin)
admin.site.register(YourModel3, YourModel3Admin)

# If you have more models, continue to add them in a similar fashion
