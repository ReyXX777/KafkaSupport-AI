from rest_framework import serializers
from .models import KafkaCluster, Topic, ConsumerGroup, Broker

class KafkaClusterSerializer(serializers.ModelSerializer):
    """
    Serializer for the KafkaCluster model.
    """
    class Meta:
        model = KafkaCluster
        fields = '__all__'  # Include all fields from the model

class TopicSerializer(serializers.ModelSerializer):
    """
    Serializer for the Topic model.
    """
    class Meta:
        model = Topic
        fields = '__all__'  # Include all fields from the model

class ConsumerGroupSerializer(serializers.ModelSerializer):
    """
    Serializer for the ConsumerGroup model.
    """
    class Meta:
        model = ConsumerGroup
        fields = '__all__'  # Include all fields from the model

class BrokerSerializer(serializers.ModelSerializer):
    """
    Serializer for the Broker model.
    """
    class Meta:
        model = Broker
        fields = '__all__'  # Include all fields from the model
