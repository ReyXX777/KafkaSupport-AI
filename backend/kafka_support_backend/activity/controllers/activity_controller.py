# activity_controller.py
from django.http import JsonResponse
from django.views import View
from .activity_service import ActivityService

class ActivityView(View):
    def get(self, request, *args, **kwargs):
        """
        Handle GET requests to retrieve activities.
        """
        try:
            activities = ActivityService.get_all_activities()
            return JsonResponse({"status": "success", "data": activities}, status=200)
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)}, status=500)
    
    def post(self, request, *args, **kwargs):
        """
        Handle POST requests to create an activity.
        """
        try:
            activity_data = request.POST
            new_activity = ActivityService.create_activity(activity_data)
            return JsonResponse({"status": "success", "data": new_activity}, status=201)
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)}, status=500)
