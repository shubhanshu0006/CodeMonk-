from django.contrib.auth import authenticate, login
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .serializers import *
from django.shortcuts import render
from .models import CustomUser
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication





class SignupPage(APIView):
    
    def post(self, request, *args, **kwargs):
        try:
            email = request.data.get("email")
            exists = CustomUser.objects.filter(email=email).exists()
            if exists:
                return Response(
                    {
                        "status": False,
                        "status_code": 400,
                        "message": "User with this email already exists.",
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )
            serializer = UserSerializer(data=request.data)
            if not serializer.is_valid():
                return Response(
                    {
                        "status": False,
                        "status_code": 400,
                        "message": "Invalid Credentials",
                        "error": serializer.errors,
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )
            serializer.save()
            context = {"subject":f"Registration Successful! Welcome to the team {serializer.data.get('name')}",
                       "context_data":f"Dear {serializer.data.get('name')}, thank you for your registration with us."
                       }
            # send_custom_email(serializer.data.get("email"),context)
            return Response(
                {
                    "status": True,
                    "status_code": 201,
                    "message": "Successfully Registered.",
                    "data": serializer.data,
                },
                status=status.HTTP_201_CREATED,
            )
        except Exception as err:
            return Response(
                {
                    "status": False,
                    "status_code": 500,
                    "message": "Something went wrong",
                    "error": str(err),
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )


@method_decorator(csrf_exempt, name="dispatch")
class LoginPage(APIView):
    
   
    def post(self, request, *args, **kwargs):
        try:
            email = request.data.get('email')
            password = request.data.get("password")
            if not email or not password:
                return Response(
                    {
                        "status": False,
                        "status_code": 400,
                        "message": "Email and password are required fields.",
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )
         
            # print(authenticate(request, username="testuser1",password="delta2024!" ))
            user = authenticate(request, email=email, password=password)
            if user is not None:
                
                login(request, user)
                token, _ = Token.objects.get_or_create(user=user) 
               
                return Response(
                    {
                        "token":token.key,
                        'success': True,
                        'message': 'Login successful',
                        
                })
            else:
                return Response(
                    {
                        "status": False,
                        "status_code": 401,
                        "message": "Invalid credentials",
                    },
                #    status=status.HTTP_401_UNAUTHORIZED, 
                )
        except Exception as err:
            return Response(
                {
                    "status": False,
                    "status_code": 500,
                    "message": "Something went wrong",
                    "error": str(err),
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )



# Create your views here.
