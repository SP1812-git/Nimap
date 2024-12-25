from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClientViewSet, ProjectViewSet, UserAssignedProjects

router = DefaultRouter()
router.register(r'clients', ClientViewSet, basename='client')
router.register(r'projects', ProjectViewSet, basename='project')

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/projects/assigned/', UserAssignedProjects.as_view(), name='user-assigned-projects'),
]
