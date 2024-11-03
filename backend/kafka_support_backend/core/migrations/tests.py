from django.test import TestCase
from django.urls import reverse
from .models import YourModel  # Replace with your actual model name

class YourModelTests(TestCase):

    def setUp(self):
        """Create a test instance of YourModel for testing."""
        self.your_model_instance = YourModel.objects.create(
            field1='Sample data',
            field2=123,
            # Add other fields as necessary
        )

    def test_your_model_str(self):
        """Test the string representation of YourModel."""
        self.assertEqual(str(self.your_model_instance), 'Expected String Representation')

    def test_your_model_field_value(self):
        """Test a specific field value in YourModel."""
        self.assertEqual(self.your_model_instance.field1, 'Sample data')

class YourModelViewTests(TestCase):

    def setUp(self):
        """Set up test data for view tests."""
        self.url = reverse('yourmodel-list')  # Update with your URL name
        self.your_model_instance = YourModel.objects.create(
            field1='Sample data',
            field2=123,
        )

    def test_view_status_code(self):
        """Test the view returns a 200 status code."""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_view_template_used(self):
        """Test the correct template is used in the view."""
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, 'yourmodel_list.html')  # Update with your template name

    def test_view_context_data(self):
        """Test that the view returns the correct context data."""
        response = self.client.get(self.url)
        self.assertIn('object_list', response.context)
        self.assertEqual(len(response.context['object_list']), 1)  # Check if the object list has one item

