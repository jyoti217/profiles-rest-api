from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.

class HelloApiView(APIView):
    """docstring for HelloApiView."""
    # def __init__(self, arg):
    #     super(HelloApiView, self).__init__()
    #     self.arg = arg

    def get(self, request, format=None):
        """Reuturns a list APIview features"""

        an_apiview = [
            'Uses HTTP methods as functions',
            'It is similiar to django view',
            'Gives you the most control over your logic',
            'Its mapped manully to URLs'
        ]

        return Response({'message':'Hello World', 'an_apiview':an_apiview});
