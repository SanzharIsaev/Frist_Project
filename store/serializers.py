from rest_framework import serializers
from .models import Store, Cart, CartItem

class StoreSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault)
    class Meta:
        model = Store
        fields = ('id', 'name', 'description', 'picture', 'price', 'user')
        

class MarketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = '__all__'

class CartItemSerializer(serializers.ModelSerializer):
    market_item = MarketSerializer()

    class Meta:
        model = CartItem
        fields = ['id', 'market_item', 'quantity']

class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True)

    class Meta:
        model = Cart
        fields = ['id', 'user', 'items']