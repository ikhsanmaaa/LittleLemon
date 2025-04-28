from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.decorators import api_view
from .models import MenuItem
from .serializers import MenuItemSerializer
from django.http import JsonResponse
from .models import MenuItem
# Create your views here.

def get_menuitem_by_title(request):
    title = request.GET.get('title')  
    try:
        item = MenuItem.objects.get(title=title)
        data = {
            'description': item.description,
            'price': str(item.price),
            'category': item.category,
        }
        return JsonResponse(data)
    except MenuItem.DoesNotExist:
        return JsonResponse({'error': 'Item not found'}, status=404)

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