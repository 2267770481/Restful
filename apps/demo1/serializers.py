from rest_framework import serializers
from apps.demo1.models import BookInfo, HeroInfo


class BookInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookInfo
        fields = "__all__"


class HeroInfoSerializer(serializers.ModelSerializer):
    hbook = serializers.CharField(source='hbook.btitle')
    bpub_date = serializers.DateField(source='hbook.bpub_date')
    bread = serializers.IntegerField(source='hbook.bread')
    bcomment = serializers.IntegerField(source='hbook.bcomment')

    class Meta:
        model = HeroInfo
        fields = "__all__"
