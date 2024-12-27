from django.apps import AppConfig

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
