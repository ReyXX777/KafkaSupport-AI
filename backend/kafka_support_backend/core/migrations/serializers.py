# commit message: Added nested serializers and custom validation to Kafka serializers

from rest_framework import serializers
from .models import KafkaCluster, Topic, ConsumerGroup, Broker

class KafkaClusterSerializer(serializers.ModelSerializer):
    """
    Serializer for the KafkaCluster model.
    """
    class Meta:
        model = KafkaCluster
        fields = '__all__'  # Include all fields from the model

    def validate_version(self, value):
        """
        Validate that the Kafka version starts with '2.'.
        """
        if not value.startswith("2."):
            raise serializers.ValidationError("Only Kafka version 2.x is supported.")
        return value

class TopicSerializer(serializers.ModelSerializer):
    """
    Serializer for the Topic model.
    """
    kafka_cluster_details = KafkaClusterSerializer(source='kafka_cluster', read_only=True)

    class Meta:
        model = Topic
        fields = '__all__'  # Include all fields from the model

    def validate_partitions(self, value):
        """
        Validate that the number of partitions is at least 1.
        """
        if value < 1:
            raise serializers.ValidationError("Number of partitions must be at least 1.")
        return value

    def validate_replication_factor(self, value):
        """
        Validate that the replication factor is at least 1.
        """
        if value < 1:
            raise serializers.ValidationError("Replication factor must be at least 1.")
        return value

class ConsumerGroupSerializer(serializers.ModelSerializer):
    """
    Serializer for the ConsumerGroup model.
    """
    kafka_cluster_details = KafkaClusterSerializer(source='kafka_cluster', read_only=True)
    topic_details = TopicSerializer(source='topic', read_only=True)

    class Meta:
        model = ConsumerGroup
        fields = '__all__'  # Include all fields from the model

    def validate_consumer_count(self, value):
        """
        Validate that the consumer count is at least 1.
        """
        if value < 1:
            raise serializers.ValidationError("Consumer count must be at least 1.")
        return value

    def validate_lag(self, value):
        """
        Validate that the lag is not negative.
        """
        if value < 0:
            raise serializers.ValidationError("Lag cannot be negative.")
        return value

class BrokerSerializer(serializers.ModelSerializer):
    """
    Serializer for the Broker model.
    """
    kafka_cluster_details = KafkaClusterSerializer(source='kafka_cluster', read_only=True)

    class Meta:
        model = Broker
        fields = '__all__'  # Include all fields from the model

    def validate_port(self, value):
        """
        Validate that the port number is between 1024 and 65535.
        """
        if value < 1024 or value > 65535:
            raise serializers.ValidationError("Port number must be between 1024 and 65535.")
        return value
