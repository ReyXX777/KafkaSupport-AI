from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from rest_framework import viewsets
from .models import YourModel  # Replace with your actual model name
from .serializers import YourModelSerializer  # Import your serializer if using DRF

# Function-based views

def your_model_list(request):
    """
    View function to display a list of YourModel instances.
    """
    your_models = YourModel.objects.all()
    return render(request, 'yourmodel_list.html', {'your_models': your_models})

def your_model_detail(request, pk):
    """
    View function to display the details of a specific YourModel instance.
    """
    your_model = get_object_or_404(YourModel, pk=pk)
    return render(request, 'yourmodel_detail.html', {'your_model': your_model})

# Class-based views using Django REST Framework

class YourModelViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing YourModel instances.
    """
    queryset = YourModel.objects.all()
    serializer_class = YourModelSerializer

    def list(self, request, *args, **kwargs):
        """
        Override the list method to customize the response.
        """
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return JsonResponse(serializer.data, safe=False)

    def retrieve(self, request, pk=None):
        """
        Override the retrieve method to return a specific object as JSON.
        """
        queryset = self.get_queryset()
        your_model = get_object_or_404(queryset, pk=pk)
        serializer = self.get_serializer(your_model)
        return JsonResponse(serializer.data)
