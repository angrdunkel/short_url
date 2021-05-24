from django.shortcuts import render

import datetime
from rest_framework import viewsets

from .models import URL
from .serializers import URLSerializer

class URLViewSet(viewsets.ModelViewSet):
    queryset = URL.objects.all()
    serializer_class = URLSerializer
