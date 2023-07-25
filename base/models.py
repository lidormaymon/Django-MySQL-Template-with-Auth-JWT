# import uuid
# from django.db import models
# from django.contrib.auth.models import User


# class Category(models.Model):
#     CategoryID = models.AutoField(primary_key=True)
#     CategoryName = models.CharField(max_length=50, null=True, blank=True)
#     Description = models.CharField(max_length=50, null=True, blank=True)

#     def __str__(self):
#         return self.Description


# class Product(models.Model):
#     ProductID = models.AutoField(primary_key=True, editable=False)
#     ProductName = models.CharField(max_length=50, null=True, blank=True)
#     CategoryID = models.ForeignKey(Category, on_delete=models.CASCADE)
#     price = models.FloatField()  
#     image = models.ImageField(null=True, blank=True, default='/placeholder.png')
#     createdTime = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.ProductName


# class Orders(models.Model):
#     OrderID = models.AutoField(primary_key=True, editable=False)
#     CustomerID = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
#     orderDate = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return str(self.OrderID)
