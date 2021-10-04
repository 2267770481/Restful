from rest_framework import serializers
from apps.demo1.models import BookInfo


# 自定义校验 需求: 添加的书籍的日期不能小于2015年
def check_bpub_date(date):
    if date.year < 2015:
        raise serializers.ValidationError("日期不能小于2015年")
    return date


class BookInfoSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True, label='主键')
    btitle = serializers.CharField(max_length=20, label='名称')
    bpub_date = serializers.DateField(label='发布日期', validators=[check_bpub_date])
    bread = serializers.IntegerField(default=0, label='阅读量')
    bcomment = serializers.IntegerField(default=0, label='评论量')
    is_delete = serializers.BooleanField(default=False, label='逻辑删除')
    # 外键反向序列化
    # heroinfo_set = serializers.PrimaryKeyRelatedField(read_only=True, many=True) # 返回id
    heroinfo_set = serializers.StringRelatedField(read_only=True, many=True)  # 返回 __str__ 内容

    # 单字段校验, 方法; 需求: 添加的书籍必须包含'along'
    def validate_btitle(self, value):
        if "along" not in value:
            raise serializers.ValidationError("书名必须包含along")
        return value

    # 多字段校验, 方法; 添加书籍的时候,评论量不能大于阅读量
    def validate(self, attrs):
        """
        :param attrs: 外界传入的需要校验的字典
        :return:
        """
        if attrs["bread"] < attrs["bcomment"]:
            raise serializers.ValidationError("评论量不能大于阅读量")
        return attrs

    def create(self, validated_data):
        # 数据入库
        book = BookInfo.objects.create(**validated_data)
        # 返回
        return book

    def update(self, instance, validated_data):
        # 数据更新
        book = instance.update(**validated_data)
        # 返回
        return book
