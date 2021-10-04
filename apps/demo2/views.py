from django.shortcuts import render
from django import http
from django.views import View
from django import http
from apps.demo1.models import BookInfo, HeroInfo
from apps.demo2.serializers import BookInfoSerializer


# Create your views here.
class BookListView(View):
    def get(self, request):
        book = BookInfo.objects.all()
        # 数据进行序列化
        books_serializer = BookInfoSerializer(instance=book, many=True)  # 序列化多个时候要用many参数
        # 返回
        return http.JsonResponse(books_serializer.data, safe=False)

    def post(self, request):
        # 获取数据
        data = request.body.decode()
        # 2,校验参数(反序列化)
        data = BookInfoSerializer(data=data)
        data.is_valid(raise_exception=True)
        # 保存数据
        book = data.save()
        # 序列化
        book_serializer = BookInfoSerializer(instance=book)
        # 返回
        return http.JsonResponse(book_serializer)


#######################################################################
"""
# 可在python manage.py shell 中输入以下进行校验 并保存
from apps.demo2.serializers import BookInfoSerializer
data_dict = {
"btitle":"along-红楼梦",
"bpub_date":"2019-01-01",
"bread":15,
"bcomment":10
}

#2,创建序列化器对象
serializer = BookInfoSerializer(data=data_dict)

#3,校验
# serializer.is_valid()
serializer.is_valid(raise_exception=True)

#4,入库
serializer.save()
"""
#######################################################################
"""
# 可在python manage.py shell 中输入以下进行校验 并更新
from apps.demo2.serializers import BookInfoSerializer
from apps.demo1.models import BookInfo
data_dict = {
"btitle":"along-红楼梦-update",
"bpub_date":"2019-01-01",
"bread":15,
"bcomment":10
}
book = BookInfo.objects.filter(pk=6)

#2,数据进行反序列化
serializer = BookInfoSerializer(instance=book, data=data_dict)

#3,校验
# serializer.is_valid()
serializer.is_valid(raise_exception=True)

#4,更新
serializer.save()
"""


#######################################################################
class BookDetailView(View):
    def get(self, request, pk):
        book = BookInfo.objects.get(pk=pk)
        # 数据进行序列化
        books_serializer = BookInfoSerializer(instance=book)
        # 返回
        return http.JsonResponse(books_serializer.data)

    def put(self, request, pk):
        # 获取数据
        data = request.body.decode()
        book = BookInfo.objects.filter(pk=pk)
        # 数据进行反序列化
        book_serializer = BookInfoSerializer(instance=book, data=data)
        # 数据校验
        book_serializer.is_valid(raise_exception=True)
        # 保存更新（注意在反序列化的时候需要传入instance和data两个数据）
        book = book_serializer.save()
        # 序列化
        book_serializer = BookInfoSerializer(instance=book)
        # 返回
        return http.JsonResponse(book_serializer)
