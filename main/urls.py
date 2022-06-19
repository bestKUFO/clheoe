from django.urls import path
from main import views
from django.conf import settings

app_name = 'main'

urlpatterns = [
    path('', views.base, name='base'),
    path('item/', views.item, name="item"),
    path('terms/', views.terms, name="terms"),
    path('membership/', views.membership, name="membership"),
    path('privacy/', views.privacy, name="privacy"),
    path('executives/', views.executives, name="executives"),
    path('service/', views.service, name="service"),
]
