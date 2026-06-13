from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status, viewsets

from apps.users.authentication.permission import IsCreator


class ProfileViewSet(viewsets.ViewSet):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated,IsCreator]

    def list(self, request):

        user=request.user

        return Response(
            {
                "username":user.username,
                "email":user.email,
            },
            status=status.HTTP_200_OK,
        )