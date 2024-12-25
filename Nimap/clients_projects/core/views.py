from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Client, Project
from .serializers import ClientSerializer, ProjectSerializer

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [IsAuthenticated]

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]

class UserAssignedProjects(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user_projects = Project.objects.filter(users=request.user)
        serializer = ProjectSerializer(user_projects, many=True)
        return Response(serializer.data)
