# commit message: Added timestamp fields and validation methods to Kafka models

from django.db import models
from django.core.exceptions import ValidationError

class KafkaCluster(models.Model):
    """
    Represents a Kafka cluster.
    """
    name = models.CharField(max_length=100, unique=True, help_text="Name of the Kafka cluster")
    version = models.CharField(max_length=20, help_text="Version of the Kafka cluster")
    location = models.CharField(max_length=100, help_text="Location or region of the Kafka cluster")
    description = models.TextField(blank=True, null=True, help_text="Description of the Kafka cluster")
    created_at = models.DateTimeField(auto_now_add=True, help_text="Timestamp when the cluster was created")
    updated_at = models.DateTimeField(auto_now=True, help_text="Timestamp when the cluster was last updated")

    def __str__(self):
        return self.name

    def clean(self):
        """
        Validate Kafka cluster data.
        """
        if self.version and not self.version.startswith("2."):
            raise ValidationError("Only Kafka version 2.x is supported.")

class Topic(models.Model):
    """
    Represents a topic within a Kafka cluster.
    """
    name = models.CharField(max_length=100, unique=True, help_text="Name of the Kafka topic")
    kafka_cluster = models.ForeignKey(KafkaCluster, on_delete=models.CASCADE, related_name='topics', help_text="Kafka cluster this topic belongs to")
    partitions = models.IntegerField(default=1, help_text="Number of partitions for the topic")
    replication_factor = models.IntegerField(default=1, help_text="Replication factor for the topic")
    retention_policy_ms = models.BigIntegerField(default=604800000, help_text="Retention policy in milliseconds (default: 7 days)")
    created_at = models.DateTimeField(auto_now_add=True, help_text="Timestamp when the topic was created")
    updated_at = models.DateTimeField(auto_now=True, help_text="Timestamp when the topic was last updated")

    def __str__(self):
        return f"{self.name} (Cluster: {self.kafka_cluster.name})"

    def clean(self):
        """
        Validate topic data.
        """
        if self.partitions < 1:
            raise ValidationError("Number of partitions must be at least 1.")
        if self.replication_factor < 1:
            raise ValidationError("Replication factor must be at least 1.")

class ConsumerGroup(models.Model):
    """
    Represents a consumer group within a Kafka cluster.
    """
    name = models.CharField(max_length=100, unique=True, help_text="Name of the consumer group")
    kafka_cluster = models.ForeignKey(KafkaCluster, on_delete=models.CASCADE, related_name='consumer_groups', help_text="Kafka cluster this consumer group belongs to")
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='consumer_groups', help_text="Topic this consumer group is subscribed to")
    consumer_count = models.IntegerField(default=1, help_text="Number of consumers in the group")
    lag = models.BigIntegerField(default=0, help_text="Current lag of the consumer group")
    created_at = models.DateTimeField(auto_now_add=True, help_text="Timestamp when the consumer group was created")
    updated_at = models.DateTimeField(auto_now=True, help_text="Timestamp when the consumer group was last updated")

    def __str__(self):
        return f"{self.name} (Cluster: {self.kafka_cluster.name}, Topic: {self.topic.name})"

    def clean(self):
        """
        Validate consumer group data.
        """
        if self.consumer_count < 1:
            raise ValidationError("Consumer count must be at least 1.")
        if self.lag < 0:
            raise ValidationError("Lag cannot be negative.")

class Broker(models.Model):
    """
    Represents a broker within a Kafka cluster.
    """
    id = models.IntegerField(primary_key=True, help_text="Unique ID of the broker")
    kafka_cluster = models.ForeignKey(KafkaCluster, on_delete=models.CASCADE, related_name='brokers', help_text="Kafka cluster this broker belongs to")
    hostname = models.CharField(max_length=100, help_text="Hostname of the broker")
    port = models.IntegerField(default=9092, help_text="Port number of the broker")
    is_active = models.BooleanField(default=True, help_text="Whether the broker is active")
    created_at = models.DateTimeField(auto_now_add=True, help_text="Timestamp when the broker was created")
    updated_at = models.DateTimeField(auto_now=True, help_text="Timestamp when the broker was last updated")

    def __str__(self):
        return f"Broker {self.id} (Cluster: {self.kafka_cluster.name}, Host: {self.hostname}:{self.port})"

    def clean(self):
        """
        Validate broker data.
        """
        if self.port < 1024 or self.port > 65535:
            raise ValidationError("Port number must be between 1024 and 65535.")
