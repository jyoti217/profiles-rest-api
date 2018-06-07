from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


from . import serializers

# Create your views here.

class HelloApiView(APIView):
    """docstring for HelloApiView."""
    # def __init__(self, arg):
    #     super(HelloApiView, self).__init__()
    #     self.arg = arg

    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Reuturns a list APIview features"""

        an_apiview = [
            'Uses HTTP methods as functions',
            'It is similiar to django view',
            'Gives you the most control over your logic',
            'Its mapped manully to URLs'
        ]

        return Response({'message':'Hello World', 'an_apiview':an_apiview});




    def post(self, request):
        """Create a hello message with our name"""
        serializer = serializers.HelloSerializer(data=request.data)
        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        """Handles updating an object"""
        return Response({'method': 'put'})

    def patch(self, request, pk=None):
        """Handles partial updating an object"""
        return Response({'method': 'patch'})

    def delete(self, request, pk=None):
        """Handles delete an object"""
        return Response({'method': 'delete'})
