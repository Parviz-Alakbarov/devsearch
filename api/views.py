from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from .serializers import ProjectSerializer, ProjectSerializerWithReviews
from projects.models import Porject



@api_view(['GET'])
def getRoutes(request):
    routes = [
        {'GET': '/api/projects'},
        {'GET': '/api/projects/id'},
        {'POST': '/api/projects/id/vote'},

        {'POST': '/api/users/token'},
        {'POST': '/api/users/token/refresh'},

    ]

    return Response(routes)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getProject(request, pk):
    project = Porject.objects.get(id=pk)
    serializer = ProjectSerializerWithReviews(project, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def getProjects(request):
    projects = Porject.objects.all()
    serializer = ProjectSerializer(projects, many=True)
    return Response(serializer.data)
