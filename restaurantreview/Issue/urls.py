# issue/urls.py
from django.urls import path
from .views import IssueListAPIView, IssueDetailAPIView

urlpatterns = [
    path('api/issues/', IssueListAPIView.as_view(), name='issue-list'),
    path('api/issues/<int:pk>/', IssueDetailAPIView.as_view(), name='issue-detail'),
    path('api/issues/<int:pk>/order/', IssueDetailAPIView.as_view(), name='issue-order'),

]