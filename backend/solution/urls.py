from django.urls import path, include
from .views import SolutionCreateView, SolutionDetailView

urlpatterns = [
    path('', SolutionCreateView.as_view(), name='solution-list'),
    path('<int:pk>/', SolutionDetailView.as_view(), name='solution-detail'),
]
