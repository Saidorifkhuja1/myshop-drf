from django.shortcuts import render, get_object_or_404
from .serializers import *
from rest_framework import generics, permissions, status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from .utils import unhash_token
from rest_framework.exceptions import NotFound



class UserRegisterApiView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegiterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user=serializer.save()
        refresh = RefreshToken.for_user(user)
        access_token = refresh.access_token
        token_data = {
            "refresh": str(refresh),
            "access": str(access_token),
        }
        return Response(token_data, status=status.HTTP_201_CREATED)


class RetrieveProfileView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer

    def get(self, request, *args, **kwargs):
        decoden_token = unhash_token(self.request.headers)
        user_id = decoden_token.get('used_id')

        if not user_id:
            raise NotFound("User not found")

        user = get_object_or_404(User, id=user_id)
        serializer = self.get_serializer(user)

        return Response(serializer.data)




