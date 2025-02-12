
import os
from django.core.wsgi import get_wsgi_application
from werkzeug.middleware.profiler import ProfilerMiddleware  # For profiling requests
from werkzeug.middleware.dispatcher import DispatcherMiddleware  # For advanced routing
from whitenoise import WhiteNoise  # For serving static files in production
from corsheaders.middleware import CorsMiddleware  # For handling CORS
from django.middleware.security import SecurityMiddleware  # For security headers

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

# Add error handling middleware
class ErrorHandlingMiddleware:
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        try:
            return self.app(environ, start_response)
        except Exception as e:
            # Log the error and return a generic error response
            print(f"Error occurred: {str(e)}")
            start_response("500 Internal Server Error", [("Content-Type", "text/plain")])
            return [b"An internal server error occurred."]

# Wrap the application with middleware
application = RequestLoggingMiddleware(application)
application = ErrorHandlingMiddleware(application)
application = CorsMiddleware(application)  # Enable CORS support
application = SecurityMiddleware(application)  # Add security headers
application = WhiteNoise(application, root=os.path.join(os.path.dirname(__file__), "staticfiles"))  # Serve static files

# Optionally enable profiling in development
if os.environ.get("DJANGO_DEBUG", "False") == "True":
    application = ProfilerMiddleware(
        application,
        profile_dir="./profiles",  # Directory to store profiling data
        restrictions=[30],  # Limit the number of functions displayed in the profile
    )

# Advanced routing with DispatcherMiddleware (optional)
application = DispatcherMiddleware(application, {
    "/api": application,  # Route API requests
    "/admin": application,  # Route admin requests
})
