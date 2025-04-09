from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.decorators import api_view
from .models import MenuItem
from .serializers import MenuItemSerializer
# Create your views here.

class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

# @api_view()
# def menu_items(request):
#     items = MenuItem.objects.all()
#     serialized_items = MenuItemSerializer(items,many = True)
#     return Response(serialized_items.data)