from django.test import TestCase
from django.urls import reverse
from .models import YourModel

class YourModelTests(TestCase):
    def setUp(self):
        self.your_model_instance = YourModel.objects.create(
            field1='Sample data',
            field2=123,
        )

    def test_your_model_str(self):
        self.assertEqual(str(self.your_model_instance), 'Expected String Representation')

    def test_your_model_field_value(self):
        self.assertEqual(self.your_model_instance.field1, 'Sample data')

class YourModelViewTests(TestCase):
    def setUp(self):
        self.url = reverse('yourmodel-list')
        self.your_model_instance = YourModel.objects.create(
            field1='Sample data',
            field2=123,
        )

    def test_view_status_code(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_view_template_used(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, 'yourmodel_list.html')

    def test_view_context_data(self):
        response = self.client.get(self.url)
        self.assertIn('object_list', response.context)
        self.assertEqual(len(response.context['object_list']), 1)
