# commit message: Added export to CSV and custom admin actions for Kafka models

from django.contrib import admin
from .models import KafkaCluster, Topic, ConsumerGroup, Broker
from django.http import HttpResponse
import csv

# Custom admin class for KafkaCluster
@admin.register(KafkaCluster)
class KafkaClusterAdmin(admin.ModelAdmin):
    # Fields to display in the list view
    list_display = ('name', 'version', 'location')
    # Fields to enable filtering
    list_filter = ('location',)
    # Fields to enable search functionality
    search_fields = ('name',)
    # Default ordering of records
    ordering = ('name',)

    # Add export to CSV action
    actions = ['export_to_csv']

    def export_to_csv(self, request, queryset):
        """
        Custom admin action to export selected Kafka clusters to CSV.
        """
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="kafka_clusters_export.csv"'
        writer = csv.writer(response)
        writer.writerow(['Name', 'Version', 'Location'])  # CSV headers
        for obj in queryset:
            writer.writerow([obj.name, obj.version, obj.location])
        return response
    export_to_csv.short_description = "Export selected clusters to CSV"

# Custom admin class for Topic
@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    # Fields to display in the list view
    list_display = ('name', 'cluster', 'partitions', 'replication_factor')
    # Fields to enable filtering
    list_filter = ('cluster',)
    # Fields to enable search functionality
    search_fields = ('name',)
    # Default ordering of records
    ordering = ('name',)

    # Add custom admin action to reset partitions
    actions = ['reset_partitions']

    def reset_partitions(self, request, queryset):
        """
        Custom admin action to reset partitions for selected topics.
        """
        queryset.update(partitions=1)
        self.message_user(request, f"Reset partitions for {queryset.count()} topics.")
    reset_partitions.short_description = "Reset partitions to 1"

# Custom admin class for ConsumerGroup
@admin.register(ConsumerGroup)
class ConsumerGroupAdmin(admin.ModelAdmin):
    # Fields to display in the list view
    list_display = ('name', 'topic', 'offset')
    # Fields to enable filtering
    list_filter = ('topic',)
    # Fields to enable search functionality
    search_fields = ('name',)
    # Default ordering of records
    ordering = ('name',)

    # Add custom admin action to reset offsets
    actions = ['reset_offsets']

    def reset_offsets(self, request, queryset):
        """
        Custom admin action to reset offsets for selected consumer groups.
        """
        queryset.update(offset=0)
        self.message_user(request, f"Reset offsets for {queryset.count()} consumer groups.")
    reset_offsets.short_description = "Reset offsets to 0"

# Custom admin class for Broker
@admin.register(Broker)
class BrokerAdmin(admin.ModelAdmin):
    # Fields to display in the list view
    list_display = ('host', 'port', 'cluster')
    # Fields to enable filtering
    list_filter = ('cluster',)
    # Fields to enable search functionality
    search_fields = ('host',)
    # Default ordering of records
    ordering = ('host',)

    # Add custom admin action to deactivate brokers
    actions = ['deactivate_brokers']

    def deactivate_brokers(self, request, queryset):
        """
        Custom admin action to mark selected brokers as inactive.
        """
        queryset.update(is_active=False)
        self.message_user(request, f"Deactivated {queryset.count()} brokers.")
    deactivate_brokers.short_description = "Deactivate selected brokers"
