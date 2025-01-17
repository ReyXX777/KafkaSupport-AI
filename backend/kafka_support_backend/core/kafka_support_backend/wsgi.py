# commit message: Added middleware for request logging and error handling

import os
from django.core.wsgi import get_wsgi_application
from werkzeug.middleware.profiler import ProfilerMiddleware  # For profiling requests
from werkzeug.middleware.dispatcher import DispatcherMiddleware  # For advanced routing

# Set the default Django settings module for the WSGI application
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "kafka_support_backend.settings")

# Create the WSGI application object
application = get_wsgi_application()

# Add request logging middleware
class RequestLoggingMiddleware:
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        # Log incoming request details
        print(f"Incoming request: {environ['REQUEST_METHOD']} {environ['PATH_INFO']}")
        return self.app(environ, start_response)

# Wrap the application with middleware
application = RequestLoggingMiddleware(application)

# Optionally enable profiling in development
if os.environ.get("DJANGO_DEBUG", "False") == "True":
    application = ProfilerMiddleware(
        application,
        profile_dir="./profiles",  # Directory to store profiling data
        restrictions=[30],  # Limit the number of functions displayed in the profile
    )
