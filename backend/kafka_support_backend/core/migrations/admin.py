from django.contrib import admin
from .models import YourModel1, YourModel2, YourModel3

class YourModel1Admin(admin.ModelAdmin):
    list_display = ('field1', 'field2', 'field3')
    search_fields = ('field1', 'field2')
    list_filter = ('field3',)

class YourModel2Admin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'is_active')
    search_fields = ('name',)
    list_filter = ('is_active',)

class YourModel3Admin(admin.ModelAdmin):
    list_display = ('title', 'updated_at')
    search_fields = ('title',)
    list_filter = ('status',)

admin.site.register(YourModel1, YourModel1Admin)
admin.site.register(YourModel2, YourModel2Admin)
admin.site.register(YourModel3, YourModel3Admin)
