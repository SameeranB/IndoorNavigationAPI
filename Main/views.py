from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from Main.functions import coords
from Main.models import Block


@api_view(['POST'])
def block_register(request):
    """
    Registers Blocks for initial database formation
    :param request:
    :return:
    """
    grid = request.data.get('result')
    dist = request.data.get('distances')
    x, y = coords(dist)
    for i in grid:
        block = Block(
            block_id=i["gid"],
            lat=i['lat'],
            lng=i['lng'],
            quad=i['quad']
        )
        block.save()
    return Response({'x': x, 'y': y}, status=201)
