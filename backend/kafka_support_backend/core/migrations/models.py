from django.db import models

class KafkaCluster(models.Model):
    name = models.CharField(max_length=100)
    # Add other relevant fields (e.g., version, location, etc.)

class Topic(models.Model):
    name = models.CharField(max_length=100)
    kafka_cluster = models.ForeignKey(KafkaCluster, on_delete=models.CASCADE)
    # Add other relevant fields (e.g., partitions, retention policy, etc.)

class ConsumerGroup(models.Model):
    name = models.CharField(max_length=100)
    kafka_cluster = models.ForeignKey(KafkaCluster, on_delete=models.CASCADE)
    # Add other relevant fields (e.g., consumer count, lag, etc.)

class Broker(models.Model):
    id = models.IntegerField(primary_key=True)
    kafka_cluster = models.ForeignKey(KafkaCluster, on_delete=models.CASCADE)
    # Add other relevant fields (e.g., hostname, port, etc.)
