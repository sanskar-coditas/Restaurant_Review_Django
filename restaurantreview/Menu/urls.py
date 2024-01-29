from django.urls import path
from .views import MenuListAPIView, MenuDetailAPIView

urlpatterns = [
    path('api/menus/', MenuListAPIView.as_view(), name='menu-list'),
    path('api/menus/<int:pk>/', MenuDetailAPIView.as_view(), name='menu-detail'),
]
