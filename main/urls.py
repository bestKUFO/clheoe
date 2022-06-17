from django.urls import path
from main import views

app_name = 'main'

urlpatterns = [
    path('', views.base, name='base'),
    # path('', 'main/detailitem.html', name="detailitem")
]