from django.contrib.auth import authenticate
from django.contrib.auth import login as django_login
from rest_framework.status import (
    HTTP_500_INTERNAL_SERVER_ERROR,
    HTTP_400_BAD_REQUEST,
    HTTP_200_OK,
)
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(["POST"])
def login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(username=username, password=password)
    if user != None and user.is_superuser:
        django_login(request, user)
        return Response(status=HTTP_200_OK)
    else:
        return Response(status=HTTP_400_BAD_REQUEST)
