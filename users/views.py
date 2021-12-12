from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
# from rest_framework_simplejwt.tokens import RefreshToken # simplejwt

from users.serializers import RegisterUserSerializer


class CustomUserCreate(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        req_serializer = RegisterUserSerializer(data=request.data)
        if req_serializer.is_valid():
            new_user = req_serializer.save()
            if new_user:
                return Response(status=status.HTTP_201_CREATED)
        return Response(req_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class BlacklistTokenView(APIView): # simplejwt
#     permission_classes = [AllowAny]
#
#     def post(self, request):
#         try:
#             refresh_token = request.data["refresh_token"]
#             token = RefreshToken(refresh_token)
#             token.blacklist()
#         except Exception as e:
#             return Response(status=status.HTTP_400_BAD_REQUEST)
