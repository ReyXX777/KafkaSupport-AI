# commit message: Added export functionality and custom admin actions

from django.contrib import admin
from .models import YourModel1, YourModel2, YourModel3
from django.http import HttpResponse
import csv

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

    # Add export to CSV action
    actions = ['export_to_csv']

    def export_to_csv(self, request, queryset):
        """
        Custom admin action to export selected records to CSV.
        """
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="yourmodel1_export.csv"'
        writer = csv.writer(response)
        writer.writerow(['Field1', 'Field2', 'Field3', 'Created At'])  # CSV headers
        for obj in queryset:
            writer.writerow([obj.field1, obj.field2, obj.field3, obj.created_at])
        return response
    export_to_csv.short_description = "Export selected records to CSV"

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

    # Add custom admin action to toggle active status
    actions = ['toggle_active_status']

    def toggle_active_status(self, request, queryset):
        """
        Custom admin action to toggle the active status of selected records.
        """
        for obj in queryset:
            obj.is_active = not obj.is_active
            obj.save()
        self.message_user(request, f"Toggled active status for {queryset.count()} records.")
    toggle_active_status.short_description = "Toggle active status"

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

    # Add custom admin action to mark as published
    actions = ['mark_as_published']

    def mark_as_published(self, request, queryset):
        """
        Custom admin action to mark selected records as published.
        """
        queryset.update(status='published')
        self.message_user(request, f"Marked {queryset.count()} records as published.")
    mark_as_published.short_description = "Mark selected as published"

# Additional customizations
admin.site.site_header = "Your Project Admin Dashboard"  # Admin panel header
admin.site.site_title = "Your Project Admin"  # Admin panel title
admin.site.index_title = "Welcome to Your Project Admin Panel"  # Admin panel index title
