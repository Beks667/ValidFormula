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
        text = request.data['formula']

        text = "".join(el for el in text if el in "〈({[]})〉")
        while text:
            flag = True
            for el in "〈〉", "()", "{}", "[]":
                if el in text:
                    text = text.replace(el, "")
                    flag = False
            if flag:
                request.data['result'] = False
                break
        else:
            request.data['result'] = True
        print(request.data)
        serializer = FormulaValidatorSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)


        # serializer = FormulaValidatorSerializers(data=request.data)
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data)
        # else:
        #     return Response(serializer.errors, status=400)


    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip
