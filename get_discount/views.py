from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import GetDiscount
from .serializers import GetDiscountSerializer


class GetDiscountAdd(viewsets.ViewSet):
    """API для оформления скидки 2+"""
    queryset = GetDiscount.objects.all()

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action == 'post':
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [AllowAny]
        return [permission() for permission in permission_classes]

    @swagger_auto_schema(request_body=GetDiscountSerializer)
    def create(self, request):
        serializer = GetDiscountSerializer(data=request.data)
        if serializer.is_valid():
            response = serializer.save(validated_data=serializer.validated_data)
            return Response(GetDiscountSerializer(response).data)
        else:
            return Response(serializer.errors)
# Create your views here.
