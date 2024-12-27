"""
Kafka Support Backend Package

This package contains modules and utilities for managing and supporting Kafka operations.
"""

# Package metadata
__version__ = "1.0.0"
__author__ = "Your Name or Team"
__email__ = "youremail@example.com"

# Expose key modules for external usage
from .settings import *  # Import settings configurations
from .urls import *      # Import URL routing definitions

# Optional initialization logic
def initialize_kafka_support_backend():
    """
    Performs any necessary initialization tasks for the Kafka Support Backend.
    For example, setting up logging or environment variables.
    """
    import logging
    logging.basicConfig(level=logging.INFO)
    logging.info("Kafka Support Backend initialized.")

# Initialize the backend when the package is imported
initialize_kafka_support_backend()
