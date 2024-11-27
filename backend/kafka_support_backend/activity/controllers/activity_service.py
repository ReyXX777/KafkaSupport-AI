class ActivityService:
    activities = []

    @staticmethod
    def get_all_activities():
        return ActivityService.activities

    @staticmethod
    def create_activity(activity_data):
        activity_id = len(ActivityService.activities) + 1
        activity = {
            "id": activity_id,
            "name": activity_data.get("name"),
            "description": activity_data.get("description")
        }
        ActivityService.activities.append(activity)
        return activity

    @staticmethod
    def update_activity(activity_id, activity_data):
        for activity in ActivityService.activities:
            if activity["id"] == activity_id:
                activity["name"] = activity_data.get("name", activity["name"])
                activity["description"] = activity_data.get("description", activity["description"])
                return activity
        raise ValueError(f"Activity with id {activity_id} not found.")

    @staticmethod
    def delete_activity(activity_id):
        for activity in ActivityService.activities:
            if activity["id"] == activity_id:
                ActivityService.activities.remove(activity)
                return
        raise ValueError(f"Activity with id {activity_id} not found.")
