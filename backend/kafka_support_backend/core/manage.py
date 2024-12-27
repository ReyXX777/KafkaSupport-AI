#!/usr/bin/env python
import os
import sys

def main():
    """
    Run administrative tasks for the Django project.
    """
    # Set the default Django settings module
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'kafka_support_backend.settings')

    try:
        # Import Django's execute_from_command_line function
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        # Handle the case where Django is not installed or not available
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    # Execute the command-line arguments using Django's management utility
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    # Run the main function when the script is executed
    main()
