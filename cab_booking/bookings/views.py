from django.shortcuts import render
from .models import Customer, Driver
from .serializers import CustomerSerializer, DriverSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class DriverView(APIView):
    def get(self,request):
        name = Driver.objects.all()
        serializer = DriverSerializer(name,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = DriverSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class DriverInfo(APIView):
    def get(self,request,id):
        try:
            obj = Driver.objects.get(id=id)
        except Driver.DoesNotExist:
            msg = {'msg':'Driver not found'}
            return Response(msg,status=status.HTTP_404_NOT_FOUND)
        serializer = DriverSerializer(obj)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def post(self,request,id):
        try:
            obj = Driver.objects.get(id=id)
        except Driver.DoesNotExist:
            msg = {'msg':'Driver not found'}
            return Response(msg,status=status.HTTP_404_NOT_FOUND)
        serializer = DriverSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    def put(self,request,id):
        try:
            obj = Driver.objects.get(id=id)
        except Driver.DoesNotExist:
            msg = {"msg":"Driver not found"}
            return Response(msg,status=status.HTTP_404_NOT_FOUND)
        serializer = DriverSerializer(obj,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_205_RESET_CONTENT)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self,request,id):
        try:
            obj = Driver.objects.get(id=id)
        except Driver.DoesNotExist:
            msg = {"msg":"Driver not found"}
            return Response(msg,status=status.HTTP_404_NOT_FOUND)
        serializer = DriverSerializer(obj,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_205_RESET_CONTENT)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk):
        try:
            name = Driver.objects.get(id=pk)
        except Driver.DoesNotExist:
            msg = {"msg":"Driver not found"}
            return Response(msg,status=status.HTTP_404_NOT_FOUND)
        name.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
class CustomerView(APIView):
    def get(self,request):
        name = Customer.objects.all()
        serializer = CustomerSerializer(name,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class CustomerInfo(APIView):
    def get(self,request,id):
        try:
            obj = Customer.objects.get(id=id)
        except Customer.DoesNotExist:
            msg = {"msg":"Customer not found"}
            return Response(msg,status=status.HTTP_404_NOT_FOUND)
        serializer = CustomerSerializer(obj)
        return Response(serializer.data)
    
    def post(self,request,id):
        try:
            obj = Customer.objects.get(id=id)
        except Customer.DoesNotExist:
            msg:{"Customer not found"}
            return Response(msg,status=status.HTTP_404_NOT_FOUND)
        serializer = CustomerSerializer(obj,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,id):
        try:
            obj = Customer.objects.get(id=id)
        except Customer.DoesNotExist:
            msg = {"msg":"Customer not found"}
            return Response(msg,status=status.HTTP_404_NOT_FOUND)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
    def put(self,request,id):
        try:
            obj = Customer.objects.get(id=id)
        except Customer.DoesNotExist:
            msg = {"msg":"Customer not found"}
            return Response(msg,status=status.HTTP_404_NOT_FOUND)
        serializer = CustomerSerializer(obj,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_205_RESET_CONTENT)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self,request,id):
        try:
            obj = Customer.objects.get(id=id)
        except Customer.DoesNotExist:
            msg = {"msg":"Customer not found"}
            return Response(msg,status=status.HTTP_404_NOT_FOUND)
        serializer = CustomerSerializer(obj,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_205_RESET_CONTENT)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)