from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import FormulaValidator
from .serializers import FormulaValidatorSerializers


class FormulaCheckViewSet(viewsets.ModelViewSet):
    serializer_class = FormulaValidatorSerializers
    queryset = FormulaValidator.objects.all()

    @action(methods=['post'], detail=False, )
    def check_formula(self, request):
        ip_client = self.get_client_ip(request)
        request.data['ip_client'] = ip_client
        serializer = FormulaValidatorSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip
