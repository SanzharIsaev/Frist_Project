from django.db import models
from django.contrib.auth.models import User

class Store(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    picture = models.ImageField(upload_to='images/')
    price = models.IntegerField(verbose_name='Цена')
    description = models.TextField(verbose_name='Описание')
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.name
    
    class Meta():
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
    

class CartItem(models.Model):
    market_item = models.ForeignKey(Store, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(CartItem)