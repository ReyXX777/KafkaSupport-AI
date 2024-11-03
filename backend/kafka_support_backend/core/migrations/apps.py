from django.apps import AppConfig

class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'  # Default field type for primary keys
    name = 'kafka_support_backend.core'  # Path to your application within the project
    verbose_name = "Kafka Support Core"  # Human-readable name for the app

    def ready(self):
        # This method is called when the app is ready, you can import signals here if needed
        import kafka_support_backend.core.signals  # Assuming you have signals to import
