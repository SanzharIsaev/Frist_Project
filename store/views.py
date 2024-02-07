from django.shortcuts import render
from .models import Store, Cart, CartItem
from rest_framework import viewsets
from .serializers import StoreSerializer, CartSerializer, CartItemSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated
from .permissions import IsAdminOrReadOnly


class StoreApiList(generics.ListCreateAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class StoreApiUpdate(generics.RetrieveUpdateAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
    permission_classes = (IsAuthenticated,)


class StoreApiDestroy(generics.RetrieveDestroyAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
    permission_classes = (IsAdminOrReadOnly,)



class CartDetailView(generics.RetrieveAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

class AddToCartView(generics.CreateAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer

class RemoveFromCartView(generics.DestroyAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer