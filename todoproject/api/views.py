from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,HttpResponse,Http404
from django.http import JsonResponse

import re

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from .serializers import taskSerializer
from .models import tasks

class taskListView(APIView):
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    def get(self,request):
        alltasks = tasks.objects.all().order_by('-id')
        serializer = taskSerializer(alltasks, many=True)
        return Response(serializer.data) 

    def post(self, request, format=None):
        serializer = taskSerializer(data=request.data)
        
        if serializer.is_valid():            
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class taskCreateView(APIView):
    
#     serializer_class = taskSerializer

#     def post(self,request):
#         try:            
#             newTask  = request.data["task"] 
            
#             regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
#             if(regex.search(newTask)==None):
#                 tasks.objects.create(task=newTask)
#                 return Response(status=status.HTTP_202_ACCEPTED)
#             else:
#                 return Response('No special characters are allowed',status=status.HTTP_400_BAD_REQUEST)
#         except:
#             return Response(status=status.HTTP_400_BAD_REQUEST)

class taskDetailsView(APIView):    
    
    def get_object(self, pk):
        try:
            return tasks.objects.get(id=pk)
        except:
            raise Http404()

    def get(self, request, pk, format=None):
        task = self.get_object(pk)
        serializer = taskSerializer(task)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        task = self.get_object(pk)
        serializer = taskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        task = self.get_object(pk)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# class userRegistrationView(GenericAPIView):
    
#     serializer_class = UserSerializer
    
#     def post(self,request):
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class userLoginView(GenericAPIView):
#     serializer_class = LoginSerializer

#     def post(self,request):
#         serializer = LoginSerializer(data=request.data)

#         user = authenticate(request,username=request.data["username"], password=request.data["password"])
    
#         if user is not None:
#             login(request, user)
#             return Response(status=status.HTTP_202_ACCEPTED)
            
#         else:
#             return Response(status=status.HTTP_400_BAD_REQUEST)