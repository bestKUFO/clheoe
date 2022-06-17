from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Order(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    search = models.TextField()  # 검색
    recent = models.TextField()  # 최근 본 상품 목록
    name = models.TextField()  # 상품 이름
    about = models.TextField()  # 상품 설명
    price = models.TextField()  # 가격
    image = models.ImageField(upload_to='photos/%Y/%m/%d', default='photos/no_image.png')  # 이미지
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated']

    def __str__(self):
        return self.author.username + ' ' + self.created.strftime('%Y-%m-%d %H:%M:%S')
