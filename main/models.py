from django.db import models


# Create your models here.

class User(models.Model):
    who = models.TextField(max_length=100)

    def __str__(self):
        return self.who


class Order(models.Model):
    gender = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="media/")  # 이미지
    title = models.TextField(max_length=100)
    name = models.TextField()  # 상품 이름
    price = models.TextField()  # 상품 가격

    def __str__(self):
        return self.name
