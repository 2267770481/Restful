from rest_framework import serializers
from apps.demo1.models import BookInfo


class BookInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookInfo
        fields = "__all__"
