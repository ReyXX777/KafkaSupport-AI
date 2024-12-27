from django.contrib import admin
from .models import YourModel1, YourModel2, YourModel3

# Custom admin class for YourModel1
class YourModel1Admin(admin.ModelAdmin):
    # Fields to display in the list view
    list_display = ('field1', 'field2', 'field3')
    # Fields to enable search functionality
    search_fields = ('field1', 'field2')
    # Fields to enable filtering
    list_filter = ('field3',)

# Custom admin class for YourModel2
class YourModel2Admin(admin.ModelAdmin):
    # Fields to display in the list view
    list_display = ('name', 'created_at', 'is_active')
    # Fields to enable search functionality
    search_fields = ('name',)
    # Fields to enable filtering
    list_filter = ('is_active',)

# Custom admin class for YourModel3
class YourModel3Admin(admin.ModelAdmin):
    # Fields to display in the list view
    list_display = ('title', 'updated_at')
    # Fields to enable search functionality
    search_fields = ('title',)
    # Fields to enable filtering
    list_filter = ('status',)

# Register models with their custom admin classes
admin.site.register(YourModel1, YourModel1Admin)
admin.site.register(YourModel2, YourModel2Admin)
admin.site.register(YourModel3, YourModel3Admin)
