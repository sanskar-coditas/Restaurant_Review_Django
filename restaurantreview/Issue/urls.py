# issue/urls.py
from django.urls import path
from .views import IssueListAPIView, IssueDetailAPIView, IssueOrderDetailsAPIView

urlpatterns = [
    path('api/issues/', IssueListAPIView.as_view(), name='issue-list'),
    path('api/issues/<int:pk>/', IssueDetailAPIView.as_view(), name='issue-detail'),
    path('api/issues/<int:id>/order/', IssueOrderDetailsAPIView.as_view(), name='issue-order'),

]