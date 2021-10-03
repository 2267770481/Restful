from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from apps.demo1.serializers import BookInfoSerializer
from apps.demo1.models import BookInfo


# Create your views here.

class BookViewSet(ModelViewSet):
    queryset = BookInfo.objects.all()
    serializer_class = BookInfoSerializer
