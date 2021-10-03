from django.shortcuts import render
from django.views import View
from django import http
import json
from apps.demo1.models import BookInfo


# Create your views here.
# 列表视图
class BookListView(View):
    def get(self, request):
        # 查询所有
        books = BookInfo.objects.all()
        # 序列化
        books_list = list()
        for book in books:
            book_dict = {
                "id": book.id,
                "btitle": book.btitle,
                "bpub_date": book.bpub_date,
                "bread": book.bread,
                "bcomment": book.bcomment,
                "is_delete": book.is_delete
            }
            books_list.append(book_dict)
        # 返回
        return http.JsonResponse(books_list, safe=False)  # safe 表示安全转换(数据为列表时才需要传)

    def post(self, request):
        # 1,获取参数
        data_dict = json.loads(request.body.decode())
        btitle = data_dict["btitle"]
        bpub_date = data_dict["bpub_date"]
        bread = data_dict["bread"]
        bcomment = data_dict["bcomment"]

        # 2,校验参数(省略)

        # 3,数据入库
        book = BookInfo.objects.create(
            btitle=btitle,
            bpub_date=bpub_date,
            bread=bread,
            bcomment=bcomment
        )

        # 序列化并返回
        book_dict = {
            "btitle": book.btitle,
            "bpub_date": book.bpub_date,
            "bread": book.bread,
            "bcomment": book.bcomment
        }
        return http.JsonResponse(book_dict, status=201)  # 状态码 201 代表保存成功


# 详情视图
class BookDetailView(View):
    def get(self, request, pk):
        # 查询单个
        book = BookInfo.objects.get(id=pk)
        # 序列化
        book_dict = {
            "id": book.id,
            "btitle": book.btitle,
            "bpub_date": book.bpub_date,
            "bread": book.bread,
            "bcomment": book.bcomment,
            "is_delete": book.is_delete
        }
        # 返回
        return http.JsonResponse(book_dict)

    def put(self, request, pk):
        # 1,获取数据,获取对象
        data_dict = json.loads(request.body.decode())
        # book = BookInfo.objects.get(id=pk)

        # 2,数据校验(省略)

        # 3,数据入库
        BookInfo.objects.filter(id=pk).update(**data_dict)
        book = BookInfo.objects.get(id=pk)

        book_dict = {
            "btitle": book.btitle,
            "bpub_date": book.bpub_date,
            "bread": book.bread,
            "bcomment": book.bcomment
        }
        # 4,返回响应
        return http.JsonResponse(book_dict, status=201)

    def delete(self, request, pk):
        # 1,删除书籍
        BookInfo.objects.get(id=pk).delete()

        # 2,返回响应
        return http.HttpResponse(status=204)
