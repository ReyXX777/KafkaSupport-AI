class ActivityService:
    """
    Service class to manage activities. This includes methods for creating,
    retrieving, updating, and deleting activities.
    """
    activities = []

    @staticmethod
    def get_all_activities():
        """
        Retrieves all activities.

        Returns:
            list: A list of all activity dictionaries.
        """
        return ActivityService.activities

    @staticmethod
    def get_activity_by_id(activity_id):
        """
        Retrieves a specific activity by its ID.

        Args:
            activity_id (int): The ID of the activity to retrieve.

        Returns:
            dict: The activity dictionary if found.

        Raises:
            ValueError: If the activity with the given ID is not found.
        """
        for activity in ActivityService.activities:
            if activity["id"] == activity_id:
                return activity
        raise ValueError(f"Activity with id {activity_id} not found.")

    @staticmethod
    def create_activity(activity_data):
        """
        Creates a new activity.

        Args:
            activity_data (dict): A dictionary containing activity details.

        Returns:
            dict: The newly created activity.
        """
        if not activity_data.get("name"):
            raise ValueError("Activity name is required.")
        if not activity_data.get("description"):
            raise ValueError("Activity description is required.")

        activity_id = len(ActivityService.activities) + 1
        activity = {
            "id": activity_id,
            "name": activity_data.get("name"),
            "description": activity_data.get("description"),
        }
        ActivityService.activities.append(activity)
        return activity

    @staticmethod
    def update_activity(activity_id, activity_data):
        """
        Updates an existing activity.

        Args:
            activity_id (int): The ID of the activity to update.
            activity_data (dict): A dictionary containing updated details.

        Returns:
            dict: The updated activity.

        Raises:
            ValueError: If the activity with the given ID is not found.
        """
        for activity in ActivityService.activities:
            if activity["id"] == activity_id:
                activity["name"] = activity_data.get("name", activity["name"])
                activity["description"] = activity_data.get(
                    "description", activity["description"]
                )
                return activity
        raise ValueError(f"Activity with id {activity_id} not found.")

    @staticmethod
    def delete_activity(activity_id):
        """
        Deletes an activity by its ID.

        Args:
            activity_id (int): The ID of the activity to delete.

        Raises:
            ValueError: If the activity with the given ID is not found.
        """
        for activity in ActivityService.activities:
            if activity["id"] == activity_id:
                ActivityService.activities.remove(activity)
                return {"message": f"Activity with id {activity_id} deleted successfully."}
        raise ValueError(f"Activity with id {activity_id} not found.")
