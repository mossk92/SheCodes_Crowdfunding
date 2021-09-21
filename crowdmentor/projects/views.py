from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Project, Pledge
from .serializers import PledgeDetailSerializer, ProjectSerializer, PledgeSerializer, ProjectDetailSerialiser
from django.http import Http404
from rest_framework import status, permissions
from .permission import IsOwnerOrReadOnly

# for /projects
class ProjectList(APIView):
    #give permission to the owner of project only others just leave read only
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

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
        print (serializer)
        # if the serializer thinks it's valid
        if serializer.is_valid():
            # save the object
            serializer.save(owner=request.user)
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
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly
    ]
    
    def get_object(self, pk):
        try:
            project = Project.objects.get(pk=pk)
            self.check_object_permissions(self.request, project)
            return project
        except Project.DoesNotExist:
            raise Http404        

    def get(self, request, pk):
        project = self.get_object(pk)
        serializer = ProjectDetailSerialiser(project)
        return Response(serializer.data)

    def put(self, request, pk):
        project = self.get_object(pk)
        data = request.data
        serializer = ProjectDetailSerialiser(
            instance=project,
            data=data,
            partial=True
        )
        if serializer.is_valid():
            serializer.save()
    
    def delete(self, request, pk, format=None):
        project = self.get_object(pk)
        project.delete()
        return Response(Status=status.HTTP_204_NO_CONTENT)

class PledgeList(APIView):
    def get(self, request):
        pledges = Pledge.objects.all()
        serializer = PledgeSerializer(pledges, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PledgeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(supporter=request.user)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

class PledgeDetail(APIView):
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly
    ]
    
    def get_object(self, pk):
        try:
            pledge = Pledge.objects.get(pk=pk)
            self.check_object_permissions(self.request, pledge)
            return pledge
        except Pledge.DoesNotExist:
            raise Http404        

    def get(self, request, pk):
        pledge = self.get_object(pk)
        serializer = PledgeDetailSerializer(pledge)
        return Response(serializer.data)

    def put(self, request, pk):
        pledge = self.get_object(pk)
        data = request.data
        serializer = PledgeDetailSerializer(
            instance=pledge,
            data=data,
            partial=True
        )
        if serializer.is_valid():
            serializer.save()
    
    def delete(self, request, pk, format=None):
        pledge = self.get_object(pk)
        pledge.delete()
        return Response(Status=status.HTTP_204_NO_CONTENT)