from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from apps.demo1.serializers import BookInfoSerializer, HeroInfoSerializer
from apps.demo1.models import BookInfo, HeroInfo


# Create your views here.

class BookViewSet(ModelViewSet):
    queryset = BookInfo.objects.all()
    serializer_class = BookInfoSerializer


class HeroViewSet(ModelViewSet):
    queryset = HeroInfo.objects.all()
    serializer_class = HeroInfoSerializer



