from rest_framework import serializers
from .models import KafkaCluster, Topic, ConsumerGroup, Broker

class KafkaClusterSerializer(serializers.ModelSerializer):
    class Meta:
        model = KafkaCluster
        fields = '__all__'

class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = '__all__'

class ConsumerGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConsumerGroup
        fields = '__all__'

class BrokerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Broker
        fields = '__all__'

  
