from django.contrib import admin
from .models import YourModel1, YourModel2, YourModel3

# Custom admin class for YourModel1
@admin.register(YourModel1)
class YourModel1Admin(admin.ModelAdmin):
    """
    Custom admin configuration for YourModel1.
    """
    list_display = ('field1', 'field2', 'field3')  # Fields displayed in the list view
    search_fields = ('field1', 'field2')  # Fields to search
    list_filter = ('field3',)  # Fields to filter
    ordering = ('field1',)  # Default ordering in admin list view
    readonly_fields = ('created_at',)  # Fields that cannot be edited in the admin

# Custom admin class for YourModel2
@admin.register(YourModel2)
class YourModel2Admin(admin.ModelAdmin):
    """
    Custom admin configuration for YourModel2.
    """
    list_display = ('name', 'created_at', 'is_active')  # Fields displayed in the list view
    search_fields = ('name',)  # Fields to search
    list_filter = ('is_active', 'created_at')  # Fields to filter
    ordering = ('-created_at',)  # Default ordering (newest first)
    readonly_fields = ('created_at', 'updated_at')  # Fields that cannot be edited in the admin
    list_editable = ('is_active',)  # Enable inline editing for specific fields

# Custom admin class for YourModel3
@admin.register(YourModel3)
class YourModel3Admin(admin.ModelAdmin):
    """
    Custom admin configuration for YourModel3.
    """
    list_display = ('title', 'status', 'updated_at')  # Fields displayed in the list view
    search_fields = ('title', 'description')  # Fields to search
    list_filter = ('status', 'updated_at')  # Fields to filter
    ordering = ('-updated_at',)  # Default ordering (newest first)
    readonly_fields = ('created_at',)  # Fields that cannot be edited in the admin
    prepopulated_fields = {'slug': ('title',)}  # Automatically generate slug based on title

    # Add advanced fieldsets for better organization
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'slug', 'description'),
        }),
        ('Status and Timestamps', {
            'fields': ('status', 'created_at', 'updated_at'),
        }),
    )

# Additional customizations
admin.site.site_header = "Your Project Admin Dashboard"  # Admin panel header
admin.site.site_title = "Your Project Admin"  # Admin panel title
admin.site.index_title = "Welcome to Your Project Admin Panel"  # Admin panel index title
