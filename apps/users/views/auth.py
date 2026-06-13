from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from apps.users.serializers.auth import LoginSerializer


class LoginViewSet(viewsets.ViewSet):
    permission_classes = [AllowAny]
    @action(methods=['post'],detail=False,url_name='login')
    def login(self,request):

        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user=serializer.validated_data['user']

        token,_=Token.objects.get_or_create(user=user)

        return Response({
            'token':token.key,
        })


