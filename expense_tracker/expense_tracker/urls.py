
from django.urls import path, include
from core import views
from rest_framework import routers

category_router = routers.SimpleRouter()
category_router.register(r"categories", views.CategoryModelViewSet, basename='category')


urlpatterns = [
    path('currencies/', views.CurrencyListAPIView.as_view(), name='currencies'),
]+ category_router.urls
