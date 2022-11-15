from django.urls import path, include
from .views import StudentListView, StudentDetailView, StudentCreateView, StudentUpdateView

urlpatterns = [
    path('list/', StudentListView.as_view(), name='student-list'),
    path('create/', StudentCreateView.as_view(), name='student-create'),
    path('detail/<int:pk>/', StudentDetailView.as_view(), name='student-detail'),
    path('update/<int:pk>/', StudentUpdateView.as_view(), name='student-detail'),
]
