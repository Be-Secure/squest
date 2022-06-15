from rest_framework.serializers import ModelSerializer
from service_catalog.models import Operation


class OperationSerializer(ModelSerializer):
    class Meta:
        model = Operation
        fields = '__all__'
        read_only = True


class AdminOperationSerializer(ModelSerializer):
    class Meta:
        model = Operation
        fields = '__all__'
