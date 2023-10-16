from rest_framework import serializers
from .models import FormulaValidator


class FormulaValidatorSerializers(serializers.ModelSerializer):
    class Meta:
        model = FormulaValidator
        fields = ['id','formula','date_of_create','result','ip_client']

        
