from django.contrib import admin
from .models import KafkaCluster, Topic, ConsumerGroup, Broker

@admin.register(KafkaCluster)
class KafkaClusterAdmin(admin.ModelAdmin):
    list_display = ('name', 'version', 'location') 
    list_filter = ('location',) 
    search_fields = ('name',) 
    ordering = ('name',)

# Similar customizations can be done for the other models.
