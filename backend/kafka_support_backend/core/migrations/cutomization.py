from django.contrib import admin
from .models import KafkaCluster, Topic, ConsumerGroup, Broker

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
