from django.db import models
from django.contrib.auth.models import User, auth

class Seller(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.IntegerField()
    address = models.TextField()
    bio = models.CharField(max_length=255)
    about = models.TextField(max_length=255)
    rating = models.IntegerField()
    business_name = models.CharField(max_length=255)
    business_category = models.CharField(max_length=255)
    business_reg_no = models.CharField(max_length=255)
    business_logo = models.ImageField(upload_to='logo_images/')

    def __str__(self):
        return self.business_name


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.IntegerField()
    address = models.TextField()

    def __str__(self):
        return self.user.username


class Product(models.Model):
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_images/', default='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS42Ibo_SzGpRMi1PRl_c0k0SVj7zSk7KGUujqu1U0S_Q&s')
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=255)
    count = models.IntegerField(default=0)
    rating = models.IntegerField()
    featured = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='OrderItem')
    created_at = models.DateTimeField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Order #{self.pk}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.product.name} - Quantity: {self.quantity}"


class Jwt(models.Model):
    user = models.OneToOneField(
        User, related_name="login_user", on_delete=models.CASCADE)
    access = models.TextField()
    refresh = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{User.objects.get(id=self.user.id)}"
