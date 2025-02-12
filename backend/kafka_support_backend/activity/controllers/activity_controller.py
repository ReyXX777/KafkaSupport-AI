from django.http import JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json
import logging
from .activity_service import ActivityService  # Ensure activity_service.py exists and contains the necessary methods.
from .models import Activity  # Assuming Activity model exists
from .serializers import ActivitySerializer  # Assuming ActivitySerializer exists
from .permissions import IsAuthenticated  # Custom permission class
from .utils import send_notification  # Utility function for sending notifications

# Set up logging
logger = logging.getLogger(__name__)

@method_decorator(csrf_exempt, name='dispatch')
class ActivityView(View):
    """
    Handles CRUD operations for activities.
    """

    def validate_activity_data(self, data):
        """
        Validate activity data.
        """
        required_fields = ['name', 'description']
        for field in required_fields:
            if field not in data:
                return False, f"Missing required field: {field}"
            if not isinstance(data[field], str):
                return False, f"Field '{field}' must be a string"
            if len(data[field]) > 255:  # Example length validation
                return False, f"Field '{field}' exceeds maximum length of 255 characters"
        return True, ""

    def get(self, request, *args, **kwargs):
        """
        Fetch all activities.
        """
        try:
            activities = ActivityService.get_all_activities()
            serializer = ActivitySerializer(activities, many=True)
            logger.info("Successfully fetched all activities")
            return JsonResponse({"status": "success", "data": serializer.data}, status=200)
        except Exception as e:
            logger.error(f"Failed to fetch activities: {str(e)}", exc_info=True)
            return JsonResponse({"status": "error", "message": "An internal error occurred"}, status=500)

    def post(self, request, *args, **kwargs):
        """
        Create a new activity.
        """
        try:
            if not IsAuthenticated.has_permission(request):
                return JsonResponse({"status": "error", "message": "Unauthorized"}, status=401)

            body = json.loads(request.body)
            if not body:
                logger.warning("Request body is empty")
                return JsonResponse({"status": "error", "message": "Request body is empty"}, status=400)
            
            is_valid, validation_message = self.validate_activity_data(body)
            if not is_valid:
                logger.warning(f"Validation failed: {validation_message}")
                return JsonResponse({"status": "error", "message": validation_message}, status=400)
            
            new_activity = ActivityService.create_activity(body)
            send_notification(f"New activity created: {new_activity['name']}")
            logger.info("Successfully created a new activity")
            return JsonResponse({"status": "success", "data": new_activity}, status=201)
        except json.JSONDecodeError:
            logger.error("Invalid JSON data")
            return JsonResponse({"status": "error", "message": "Invalid JSON data"}, status=400)
        except Exception as e:
            logger.error(f"Failed to create activity: {str(e)}", exc_info=True)
            return JsonResponse({"status": "error", "message": "An internal error occurred"}, status=500)

    def put(self, request, *args, **kwargs):
        """
        Update an existing activity identified by `activity_id`.
        """
        try:
            if not IsAuthenticated.has_permission(request):
                return JsonResponse({"status": "error", "message": "Unauthorized"}, status=401)

            activity_id = kwargs.get('activity_id')
            if not activity_id:
                logger.warning("Activity ID is required")
                return JsonResponse({"status": "error", "message": "Activity ID is required"}, status=400)

            body = json.loads(request.body)
            if not body:
                logger.warning("Request body is empty")
                return JsonResponse({"status": "error", "message": "Request body is empty"}, status=400)
            
            is_valid, validation_message = self.validate_activity_data(body)
            if not is_valid:
                logger.warning(f"Validation failed: {validation_message}")
                return JsonResponse({"status": "error", "message": validation_message}, status=400)
            
            updated_activity = ActivityService.update_activity(activity_id, body)
            send_notification(f"Activity updated: {updated_activity['name']}")
            logger.info(f"Successfully updated activity with ID: {activity_id}")
            return JsonResponse({"status": "success", "data": updated_activity}, status=200)
        except json.JSONDecodeError:
            logger.error("Invalid JSON data")
            return JsonResponse({"status": "error", "message": "Invalid JSON data"}, status=400)
        except Exception as e:
            logger.error(f"Failed to update activity: {str(e)}", exc_info=True)
            return JsonResponse({"status": "error", "message": "An internal error occurred"}, status=500)

    def delete(self, request, *args, **kwargs):
        """
        Delete an activity identified by `activity_id`.
        """
        try:
            if not IsAuthenticated.has_permission(request):
                return JsonResponse({"status": "error", "message": "Unauthorized"}, status=401)

            activity_id = kwargs.get('activity_id')
            if not activity_id:
                logger.warning("Activity ID is required")
                return JsonResponse({"status": "error", "message": "Activity ID is required"}, status=400)

            activity = ActivityService.get_activity_by_id(activity_id)
            ActivityService.delete_activity(activity_id)
            send_notification(f"Activity deleted: {activity['name']}")
            logger.info(f"Successfully deleted activity with ID: {activity_id}")
            return JsonResponse({"status": "success", "message": "Activity deleted successfully"}, status=200)
        except Exception as e:
            logger.error(f"Failed to delete activity: {str(e)}", exc_info=True)
            return JsonResponse({"status": "error", "message": "An internal error occurred"}, status=500)
