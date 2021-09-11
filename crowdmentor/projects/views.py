from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Project, Pledge
from .serializers import ProjectSerializer, PledgeSerializer, ProjectDetailSerialiser
from django.http import Http404
from rest_framework import status

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
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.data,
            status=status.HTTP_400_BAD_REQUEST
        )

class ProjectDetail(APIView):
    def get_object(self, pk):
        try:
            return Project.objects.get(pk=pk)
        except Project.DoesNotExist:
            raise Http404        

    def get(self, request, pk):
        project = self.get_object(pk)
        serializer = ProjectDetailSerialiser(project)
        return Response(serializer.data)

class PledgeList(APIView):
    def get(self, request):
        pledges = Pledge.objects.all()
        serializer = PledgeSerializer(pledges, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PledgeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )