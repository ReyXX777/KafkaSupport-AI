from django.test import TestCase
from django.urls import reverse
from .models import YourModel

class YourModelTests(TestCase):
    """
    Test cases for the YourModel model.
    """
    def setUp(self):
        """
        Set up test data for the model.
        """
        self.your_model_instance = YourModel.objects.create(
            field1='Sample data',
            field2=123,
        )

    def test_your_model_str(self):
        """
        Test the string representation of the model.
        """
        expected_str = f"{self.your_model_instance.field1} - {self.your_model_instance.field2}"
        self.assertEqual(str(self.your_model_instance), expected_str)

    def test_your_model_field_value(self):
        """
        Test the value of a specific field in the model.
        """
        self.assertEqual(self.your_model_instance.field1, 'Sample data')

class YourModelViewTests(TestCase):
    """
    Test cases for the views associated with YourModel.
    """
    def setUp(self):
        """
        Set up test data and URLs for the views.
        """
        self.url = reverse('yourmodel-list')  # URL for the list view
        self.your_model_instance = YourModel.objects.create(
            field1='Sample data',
            field2=123,
        )

    def test_view_status_code(self):
        """
        Test that the view returns a 200 status code.
        """
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_view_template_used(self):
        """
        Test that the correct template is used by the view.
        """
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, 'yourmodel_list.html')

    def test_view_context_data(self):
        """
        Test that the view passes the correct context data.
        """
        response = self.client.get(self.url)
        self.assertIn('object_list', response.context)  # Check if 'object_list' is in the context
        self.assertEqual(len(response.context['object_list']), 1)  # Check if the context contains exactly one object
