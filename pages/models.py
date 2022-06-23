from django.db import models
from django.utils import timezone

from users.models import CustomUser


class Category(models.Model):
    CATEGORY_CHOICES = [
        ('Telefonlar', 'Telefon'),
        ('Noutbuklar', 'Noutbuk'),
        ('Mashinalar', 'Mashina'),
        ('Hayvonlar', 'Hayvon'),
        ('Uylar', 'Uy'),
        ('Mebellar', 'Mebel')
    ]
    name = models.CharField(max_length=60, choices=CATEGORY_CHOICES)
    picture = models.ImageField(null=True, blank=True)
    def __str__(self):
        return self.name

class Product(models.Model):
    ADRESS_CHOICES = [
        ('Toshkent', 'Toshkent'),
        ('Andijon', 'Andijon'),
        ('Xorazm', 'Xorazm'),
        ('Buxoro', 'Buxoro'),
        ('Samarqand', 'Samarqand'),
        ('Qashqadaryo', 'Qashqadaryo'),
        ('Surxondaryo', 'Surxondaryo'),
        ('Namangan', 'Namangan'),
        ('Sirdaryo', 'Sirdaryo'),
        ('Jizzax', 'Jizzax'),
        ('Navoiy', 'Navoiy'),
        ("Qoraqalpog'iston", "Qoraqalpog'iston"),
        ("Farg'ona", "Farg'ona"),
        ("Marg'ilon", "Marg'ilon"),
        ("Qo'qon", "Qo'qon"),
        ]

    name = models.CharField(max_length=60)
    description = models.CharField(max_length=250)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    picture = models.ImageField(default='default.png')
    price = models.PositiveIntegerField()
    adress = models.CharField(max_length=60, choices=ADRESS_CHOICES, null=True, blank=True)
    username = models.CharField(max_length=60)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

class Likes(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.user} {self.product} '