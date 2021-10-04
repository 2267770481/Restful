from django.shortcuts import render
from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import ModelViewSet
from apps.demo1.serializers import BookInfoSerializer, HeroInfoSerializer
from apps.demo1.models import BookInfo, HeroInfo


# Create your views here.

class BookViewSet(ModelViewSet):
    """
    图书视图
    """
    queryset = BookInfo.objects.all()
    serializer_class = BookInfoSerializer
    permission_classes = (IsAdminUser,)


class HeroViewSet(ModelViewSet):
    """
    英雄视图
    """
    queryset = HeroInfo.objects.all()
    serializer_class = HeroInfoSerializer
