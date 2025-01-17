# commit message: Added activity validation and logging components to ActivityService

import logging

class ActivityService:
    """
    Service class to manage activities. This includes methods for creating,
    retrieving, updating, and deleting activities.
    """
    activities = []

    # Set up logging
    logger = logging.getLogger(__name__)

    @staticmethod
    def validate_activity_data(activity_data):
        """
        Validates activity data for required fields.

        Args:
            activity_data (dict): A dictionary containing activity details.

        Returns:
            tuple: (bool, str) indicating validation success and error message if any.
        """
        required_fields = ['name', 'description']
        for field in required_fields:
            if not activity_data.get(field):
                return False, f"Missing required field: {field}"
        return True, ""

    @staticmethod
    def get_all_activities():
        """
        Retrieves all activities.

        Returns:
            list: A list of all activity dictionaries.
        """
        ActivityService.logger.info("Retrieving all activities")
        return ActivityService.activities

    @staticmethod
    def get_activity_by_id(activity_id):
        """
        Retrieves a specific activity by its ID.

        Args:
            activity_id (int): The ID of the activity to retrieve.

        Returns:
            dict: The activity dictionary if found, or None if not found.

        Raises:
            ValueError: If the activity with the given ID is not found.
        """
        ActivityService.logger.info(f"Retrieving activity with ID: {activity_id}")
        activity = next((act for act in ActivityService.activities if act["id"] == activity_id), None)
        if activity is None:
            ActivityService.logger.error(f"Activity with ID {activity_id} not found")
            raise ValueError(f"Activity with id {activity_id} not found.")
        return activity

    @staticmethod
    def create_activity(activity_data):
        """
        Creates a new activity.

        Args:
            activity_data (dict): A dictionary containing activity details.

        Returns:
            dict: The newly created activity.

        Raises:
            ValueError: If required fields are missing.
        """
        ActivityService.logger.info("Creating a new activity")
        is_valid, validation_message = ActivityService.validate_activity_data(activity_data)
        if not is_valid:
            ActivityService.logger.error(f"Validation failed: {validation_message}")
            raise ValueError(validation_message)

        # Generate a unique ID for the new activity
        activity_id = (ActivityService.activities[-1]["id"] + 1) if ActivityService.activities else 1
        activity = {
            "id": activity_id,
            "name": activity_data.get("name"),
            "description": activity_data.get("description"),
        }
        ActivityService.activities.append(activity)
        ActivityService.logger.info(f"Successfully created activity with ID: {activity_id}")
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
        ActivityService.logger.info(f"Updating activity with ID: {activity_id}")
        for activity in ActivityService.activities:
            if activity["id"] == activity_id:
                # Update only fields provided in `activity_data`
                activity["name"] = activity_data.get("name", activity["name"])
                activity["description"] = activity_data.get("description", activity["description"])
                ActivityService.logger.info(f"Successfully updated activity with ID: {activity_id}")
                return activity
        ActivityService.logger.error(f"Activity with ID {activity_id} not found")
        raise ValueError(f"Activity with id {activity_id} not found.")

    @staticmethod
    def delete_activity(activity_id):
        """
        Deletes an activity by its ID.

        Args:
            activity_id (int): The ID of the activity to delete.

        Returns:
            dict: Confirmation message upon successful deletion.

        Raises:
            ValueError: If the activity with the given ID is not found.
        """
        ActivityService.logger.info(f"Deleting activity with ID: {activity_id}")
        activity = next((act for act in ActivityService.activities if act["id"] == activity_id), None)
        if activity is None:
            ActivityService.logger.error(f"Activity with ID {activity_id} not found")
            raise ValueError(f"Activity with id {activity_id} not found.")
        
        ActivityService.activities.remove(activity)
        ActivityService.logger.info(f"Successfully deleted activity with ID: {activity_id}")
        return {"message": f"Activity with id {activity_id} deleted successfully."}
