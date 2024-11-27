from django.http import JsonResponse
from django.views import View
import json
from .activity_service import ActivityService

class ActivityModule(View):
    def get(self, request, *args, **kwargs):
        try:
            activities = ActivityService.get_all_activities()
            return JsonResponse({"status": "success", "data": activities}, status=200)
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)}, status=500)

    def post(self, request, *args, **kwargs):
        try:
            body = json.loads(request.body)
            new_activity = ActivityService.create_activity(body)
            return JsonResponse({"status": "success", "data": new_activity}, status=201)
        except json.JSONDecodeError:
            return JsonResponse({"status": "error", "message": "Invalid JSON data"}, status=400)
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)}, status=500)

    def put(self, request, activity_id, *args, **kwargs):
        try:
            body = json.loads(request.body)
            updated_activity = ActivityService.update_activity(activity_id, body)
            return JsonResponse({"status": "success", "data": updated_activity}, status=200)
        except json.JSONDecodeError:
            return JsonResponse({"status": "error", "message": "Invalid JSON data"}, status=400)
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)}, status=500)

    def delete(self, request, activity_id, *args, **kwargs):
        try:
            ActivityService.delete_activity(activity_id)
            return JsonResponse({"status": "success", "message": "Activity deleted successfully"}, status=200)
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)}, status=500)
