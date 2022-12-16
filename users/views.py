from rest_framework.views import APIView, Request, Response, status
from .models import User
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import UserSerializer
from django.shortcuts import get_object_or_404
from .permissions import IsAccountOwner
from rest_framework import generics

from rest_framework.permissions import IsAuthenticated


class UserView(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserDetailView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwner]

    def get(self, request: Request, pk: int) -> Response:
        """
        Obtençao de usuário
        """
        user = get_object_or_404(User, pk=pk)

        self.check_object_permissions(request, user)

        serializer = UserSerializer(user)

        return Response(serializer.data)

    def patch(self, request: Request, pk: int) -> Response:
        """
        Atualização de usuário
        """
        user = get_object_or_404(User, pk=pk)

        self.check_object_permissions(request, user)

        serializer = UserSerializer(user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)

    def delete(self, request: Request, pk: int) -> Response:
        """
        Deleçao de usuário
        """
        user = get_object_or_404(User, pk=pk)

        self.check_object_permissions(request, user)

        user.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)