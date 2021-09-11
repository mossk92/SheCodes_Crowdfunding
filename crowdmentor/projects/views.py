from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Project
from .serializers import ProjectSerializer

# for /projects
class ProjectList(APIView):

    # for GET /projects
    def get(self, request):
        # get all the projects
        projects = Project.objects.all()
        # serialise all the projects
        serializer = ProjectSerializer(projects, many=True)
        # send all the serialised projects back in response body
        return Response(serializer.data)

    # for POST /projects
    def post(self, request):
        # try to create a serilzer from the data in the request body
        serializer = ProjectSerializer(data=request.data)
        # if the serializer thinks it's valid
        if serializer.is_valid():
            # save the object
            serializer.save()
            # send the serialized (saved) data back in response data
            return Response(serializer.data)