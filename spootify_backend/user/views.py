from django.shortcuts import render
from rest_framework.decorators import api_view
from .serializers import(
    RegisterSerializer,
    CustomerInfoSerializer
)
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User

# Create your views here.

@api_view(['POST'])
def register_view(request):
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
@api_view(['POST'])
def login_view(request):
    user_info = request.data.get('user_info')
    password = request.data.get('password')
    if '@' in user_info:
        user = User.objects.filter(email=user_info).first()
    else:
        user = User.objects.filter(username=user_info).first()

    if user and user.check_password(password):
        serializer = CustomerInfoSerializer(instance=user.customer)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    return Response(data={'message':'User info or password is incorrect !'}, status=status.HTTP_400_BAD_REQUEST)

