from django.urls import path, include
from .views import CourseListView, CourseDetailView, CourseUpdateView, CourseCreateView

urlpatterns = [
    path('create/', CourseCreateView.as_view(), name='course-create'),
    path('list/', CourseListView.as_view(), name='course-list'),
    path('update/<int:pk>/', CourseUpdateView.as_view(), name='course-update'),
    path('detail/<int:pk>/', CourseDetailView.as_view(), name='course-detail'),
]
