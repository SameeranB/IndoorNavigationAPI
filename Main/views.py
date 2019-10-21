from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from Main.serializers import BlockRegisterSerializer




@api_view(['POST'])
def post(request):
    """
    Registers Blocks for initial database formation
    :param request:
    :return:
    """
    serializer = BlockRegisterSerializer(request.data)
    if serializer.is_valid():
        serializer.save()
        dist = serializer.validated_data.get('distances')
        x,y = coords(dist)
        return Response(status=201)
    else:
        return Response(status=400)
