from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication,permissions
from.serializer import *
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
##
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from django.contrib.auth.hashers import check_password
# from .models import UserProfile, UserSession
from rest_framework.authtoken.models import Token
from django.utils import timezone

# Create your views here.
class SignupView(APIView):
    @swagger_auto_schema(operation_description="User creation for an organisation",request_body=UserSerializer,
    responses={200: "{'status':True,'message': 'User created successfully'}",400:"Passes an error message"})
    def post(self,request):
        seria=UserSerializer(data=request.data)
        if seria.is_valid():
            seria.save()
            return Response(data=seria.data)
        else:
            return Response(data=seria.errors)
class LoginView(APIView):
    # @swagger_auto_schema(
    #     operation_description="Login authentication using username and password, and return token",
    #     request_body=openapi.Schema(
    #         type=openapi.TYPE_OBJECT,
    #         required=['username', 'password'],
    #         properties={
    #             'username': openapi.Schema(type=openapi.TYPE_STRING, description='Username for authentication'),
    #             'password': openapi.Schema(type=openapi.TYPE_STRING, description='Password for authentication')
    #         }
    #     ),
    #     responses={
    #         200: openapi.Response(
    #             description="Successful authentication and token generation",
    #             examples={
    #                 'application/json': {
    #                     "status": True,
    #                     "token": "d08dcdfssd38ffaaa0d974fb7379e05ec1cd5b95"
    #                 }
    #             }
    #         ),
    #         400: openapi.Response(
    #             description="Invalid credentials or blocked user",
    #             examples={
    #                 'application/json': {
    #                     "status": False,
    #                     "message": "Invalid credentials"
    #                 }
    #             }
    #         ),
    #         403: openapi.Response(
    #             description="User is blocked",
    #             examples={
    #                 'application/json': {
    #                     "status": False,
    #                     "message": "User Blocked"
    #                 }
    #             }
    #         )
    #     }
    # )
    @swagger_auto_schema(operation_description="Login authentication using username and password, and return token",
        request_body=openapi.Schema(type=openapi.TYPE_OBJECT,required=['username', 'password'],
        properties={'username': openapi.Schema(type=openapi.TYPE_STRING, description='Username for authentication'),'password': openapi.Schema(type=openapi.TYPE_STRING, description='Password for authentication'),},),
        responses={200: '{"status": true,"token": "d08dcdfssd38ffaaa0d974fb7379e05ec1cd5b95"}',400:'{"status": false,"message": "Invalid credentials"}'}
    )
    def post(self,request,*args,**kwargs):
        username=request.data['username']    
        password=request.data['password']
        user=authenticate(username=username,password=password)
        if user:
            token,created=Token.objects.get_or_create(user=user)
            return Response({
                'user':UserSerializer(user).data,
                'token':token.key})
        
        return Response(data="invalid")   
        
        
class QuestionView(APIView):
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    @swagger_auto_schema(
        operation_description='user can post question ',request_body=QuestionSerializer,
        responses={200: "{'status':True,'message': 'User created successfully'}",400:"Passes an error message"}
    )
    def post(self,request):
        ser=QuestionSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(data=ser.data)
        else:
            return Response(data=ser.errors)
class AnswerView(APIView)    :
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    @swagger_auto_schema(
        operation_description="Post answers to the specific question",
        request_body=AnswerSerializer,
        responses={200:"{'staus': True,'message':'answer is posted successfully'}"}
        
    )
    def post(self,request,*ars,**kw):
        id=kw.get('id')
        question=Question.objects.get(id=id)
        ser=AnswerSerializer(data=request.data)
        if ser.is_valid():
            ser.save(question=question)
            return Response(data=ser.data)
        else:
            return Response(data=ser.errors)
        
# class 