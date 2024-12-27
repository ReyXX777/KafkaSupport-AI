from django.http import JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json
from .activity_service import ActivityService


@method_decorator(csrf_exempt, name='dispatch')
class ActivityModule(View):
    """
    A class-based view for managing activity-related operations, including
    creating, retrieving, updating, and deleting activities.
    """

    def get(self, request, *args, **kwargs):
        """
        Handles GET requests to retrieve all activities or a specific activity if `activity_id` is provided.
        """
        try:
            activity_id = kwargs.get('activity_id')
            if activity_id:
                # Fetch a specific activity by ID
                activity = ActivityService.get_activity_by_id(activity_id)
                if not activity:
                    return JsonResponse(
                        {"status": "error", "message": "Activity not found"},
                        status=404
                    )
                return JsonResponse({"status": "success", "data": activity}, status=200)

            # Fetch all activities
            activities = ActivityService.get_all_activities()
            return JsonResponse({"status": "success", "data": activities}, status=200)
        except Exception as e:
            return JsonResponse(
                {"status": "error", "message": f"Error retrieving activities: {str(e)}"},
                status=500
            )

    def post(self, request, *args, **kwargs):
        """
        Handles POST requests to create a new activity.
        """
        try:
            body = json.loads(request.body)
            new_activity = ActivityService.create_activity(body)
            return JsonResponse({"status": "success", "data": new_activity}, status=201)
        except json.JSONDecodeError:
            return JsonResponse(
                {"status": "error", "message": "Invalid JSON data"},
                status=400
            )
        except Exception as e:
            return JsonResponse(
                {"status": "error", "message": f"Error creating activity: {str(e)}"},
                status=500
            )

    def put(self, request, *args, **kwargs):
        """
        Handles PUT requests to update an existing activity by ID.
        """
        try:
            activity_id = kwargs.get('activity_id')
            if not activity_id:
                return JsonResponse(
                    {"status": "error", "message": "Activity ID is required"},
                    status=400
                )
            body = json.loads(request.body)
            updated_activity = ActivityService.update_activity(activity_id, body)
            if not updated_activity:
                return JsonResponse(
                    {"status": "error", "message": "Activity not found"},
                    status=404
                )
            return JsonResponse({"status": "success", "data": updated_activity}, status=200)
        except json.JSONDecodeError:
            return JsonResponse(
                {"status": "error", "message": "Invalid JSON data"},
                status=400
            )
        except Exception as e:
            return JsonResponse(
                {"status": "error", "message": f"Error updating activity: {str(e)}"},
                status=500
            )

    def delete(self, request, *args, **kwargs):
        """
        Handles DELETE requests to remove an activity by ID.
        """
        try:
            activity_id = kwargs.get('activity_id')
            if not activity_id:
                return JsonResponse(
                    {"status": "error", "message": "Activity ID is required"},
                    status=400
                )
            success = ActivityService.delete_activity(activity_id)
            if not success:
                return JsonResponse(
                    {"status": "error", "message": "Activity not found"},
                    status=404
                )
            return JsonResponse(
                {"status": "success", "message": "Activity deleted successfully"},
                status=200
            )
        except Exception as e:
            return JsonResponse(
                {"status": "error", "message": f"Error deleting activity: {str(e)}"},
                status=500
            )
