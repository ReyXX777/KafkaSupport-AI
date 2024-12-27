from django.http import JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json
from .activity_service import ActivityService

@method_decorator(csrf_exempt, name='dispatch')
class ActivityView(View):
    """
    Handles CRUD operations for activities.
    """

    def get(self, request, *args, **kwargs):
        """
        Fetch all activities.
        """
        try:
            activities = ActivityService.get_all_activities()
            return JsonResponse({"status": "success", "data": activities}, status=200)
        except Exception as e:
            return JsonResponse({"status": "error", "message": f"Failed to fetch activities: {str(e)}"}, status=500)

    def post(self, request, *args, **kwargs):
        """
        Create a new activity.
        """
        try:
            body = json.loads(request.body)
            new_activity = ActivityService.create_activity(body)
            return JsonResponse({"status": "success", "data": new_activity}, status=201)
        except json.JSONDecodeError:
            return JsonResponse({"status": "error", "message": "Invalid JSON data"}, status=400)
        except Exception as e:
            return JsonResponse({"status": "error", "message": f"Failed to create activity: {str(e)}"}, status=500)

    def put(self, request, *args, **kwargs):
        """
        Update an existing activity identified by `activity_id`.
        """
        try:
            activity_id = kwargs.get('activity_id')
            if not activity_id:
                return JsonResponse({"status": "error", "message": "Activity ID is required"}, status=400)
            
            body = json.loads(request.body)
            updated_activity = ActivityService.update_activity(activity_id, body)
            return JsonResponse({"status": "success", "data": updated_activity}, status=200)
        except json.JSONDecodeError:
            return JsonResponse({"status": "error", "message": "Invalid JSON data"}, status=400)
        except Exception as e:
            return JsonResponse({"status": "error", "message": f"Failed to update activity: {str(e)}"}, status=500)

    def delete(self, request, *args, **kwargs):
        """
        Delete an activity identified by `activity_id`.
        """
        try:
            activity_id = kwargs.get('activity_id')
            if not activity_id:
                return JsonResponse({"status": "error", "message": "Activity ID is required"}, status=400)

            ActivityService.delete_activity(activity_id)
            return JsonResponse({"status": "success", "message": "Activity deleted successfully"}, status=200)
        except Exception as e:
            return JsonResponse({"status": "error", "message": f"Failed to delete activity: {str(e)}"}, status=500)
