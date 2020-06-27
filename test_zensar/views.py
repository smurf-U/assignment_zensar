
import json

from django.http import JsonResponse

from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView 
from rest_framework import viewsets
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework import status
from .serializer import RouterManagerSerializer


from .models import RouterManager


def search_router(request, **kwarg):
    data = json.loads(request.body)
    if data.get('hostname'):
        router_data = RouterManager.objects.filter(hostname__contains=data.get('hostname'))
    elif data.get('f_ipv4') and data.get('t_ipv4'):
        router_data = RouterManager.objects.filter(hostname__contains=data.get('hostname'))
    else:
        router_data = RouterManager.objects.all()

    
    return JsonResponse([{
        'id': router.id, 
        'sapid': router.sapid, 
        'hostname': router.hostname, 
        'loopback': router.loopback, 
        'mac_address': router.mac_address, 
        } for router in router_data], safe=False)

class RouterManagerList(ListView): 
    model = RouterManager
    template_name = 'router/list.html'
    context_object_name = 'routers'

class RouterManagerDetail(DetailView): 
    model = RouterManager
    template_name = 'router/detail.html'
    context_object_name = 'router'

class RouterManagerCreate(CreateView): 
    model = RouterManager
    template_name = 'router/create.html'
    fields = "__all__"
    success_url = reverse_lazy('routermanager_list')

class RouterManagerUpdate(UpdateView): 
    model = RouterManager
    template_name = 'router/update.html'
    context_object_name = 'router'
    fields = "__all__"

    def get_success_url(self):
        return reverse_lazy('routermanager_detail', kwargs={'pk': self.object.id})

class RouterManagerDelete(DeleteView): 
    model = RouterManager
    template_name = 'router/delete.html'
    success_url = reverse_lazy('routermanager_list')

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def delete_router_based_on_ip(request):
    try:
        ip = request.query_params.get('ip', None)
        router = RouterManager.objects.get(loopback=ip)
    except RouterManager.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    router.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def router_list(request):
    """
    List all code Router, or create a new Router.
    """
    if request.method == 'GET':
        sapid = request.query_params.get('sapid', None)
        if sapid is not None:
            router = RouterManager.objects.filter(sapid__contains=sapid)
        else:
            router = RouterManager.objects.all()
        serializer = RouterManagerSerializer(router, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = RouterManagerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def router_detail(request, pk):
    """
    Retrieve, update or delete a code router.
    """
    try:
        router = RouterManager.objects.get(pk=pk)
    except RouterManager.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = RouterManagerSerializer(router)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = RouterManagerSerializer(router, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        router.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def api_list(request):
    return Response({
        'router_list_create': 'api/router/',
        'router_detail_update_delete': 'api/router/{int:id}',
        'router_delete_base_on_ip': 'api/router/delete_base_on_ip?ip={str:ip}',
    },status=status.HTTP_200_OK)






