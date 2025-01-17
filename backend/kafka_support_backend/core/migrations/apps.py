# commit message: Added Kafka consumer initialization and custom app configuration

from django.apps import AppConfig
from kafka import KafkaConsumer  # Kafka consumer for real-time data processing
import threading
import logging

# Set up logging
logger = logging.getLogger(__name__)

class CoreConfig(AppConfig):
    # Default field type for primary keys
    default_auto_field = 'django.db.models.BigAutoField'

    # Path to your application within the project
    name = 'kafka_support_backend.core'

    # Human-readable name for the app
    verbose_name = "Kafka Support Core"

    def ready(self):
        """
        This method is called when the app is ready.
        You can import signals or perform other initialization tasks here.
        """
        # Import signals if they exist
        import kafka_support_backend.core.signals

        # Initialize Kafka consumer in a separate thread
        self.start_kafka_consumer()

    def start_kafka_consumer(self):
        """
        Start a Kafka consumer to listen for messages in a separate thread.
        """
        def kafka_consumer_loop():
            try:
                consumer = KafkaConsumer(
                    bootstrap_servers=os.environ.get("KAFKA_BOOTSTRAP_SERVERS", "localhost:9092"),
                    group_id="kafka_support_group",
                    auto_offset_reset="earliest",
                    enable_auto_commit=True,
                    value_deserializer=lambda x: x.decode("utf-8"),
                )
                consumer.subscribe(topics=["activity_topic"])  # Subscribe to the activity topic

                logger.info("Kafka consumer started successfully.")
                for message in consumer:
                    logger.info(f"Received Kafka message: {message.value}")
                    # Process the message here (e.g., save to database or trigger an action)

            except Exception as e:
                logger.error(f"Error in Kafka consumer: {str(e)}")

        # Start the Kafka consumer in a separate thread
        kafka_thread = threading.Thread(target=kafka_consumer_loop, daemon=True)
        kafka_thread.start()
        logger.info("Kafka consumer thread started.")
