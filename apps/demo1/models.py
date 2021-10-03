from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
# 定义图书模型类BookInfo
class BookInfo(models.Model):
    btitle = models.CharField(max_length=20, verbose_name=_('名称'))
    bpub_date = models.DateField(verbose_name=_('发布日期'))
    bread = models.IntegerField(default=0, verbose_name=_('阅读量'))
    bcomment = models.IntegerField(default=0, verbose_name=_('评论量'))
    is_delete = models.BooleanField(default=False, verbose_name=_('逻辑删除'))

    class Meta:
        db_table = 'tb_books'  # 指明数据库表名
        verbose_name = _('图书')  # 在admin站点中显示的名称
        verbose_name_plural = _(verbose_name)  # 显示的复数名称

    def __str__(self):
        """定义每个数据对象的显示信息"""
        return self.btitle


# 定义英雄模型类HeroInfo
class HeroInfo(models.Model):
    GENDER_CHOICES = (
        (0, 'male'),
        (1, 'female')
    )
    hname = models.CharField(max_length=20, verbose_name=_('名称'))
    hgender = models.SmallIntegerField(choices=GENDER_CHOICES, default=0, verbose_name=_('性别'))
    hcomment = models.CharField(max_length=200, null=True, verbose_name=_('描述信息'))
    hbook = models.ForeignKey(BookInfo, on_delete=models.CASCADE, verbose_name=_('图书'))  # 外键
    is_delete = models.BooleanField(default=False, verbose_name=_('逻辑删除'))

    class Meta:
        db_table = 'tb_heros'
        verbose_name = _('英雄')
        verbose_name_plural = _(verbose_name)

    def __str__(self):
        return self.hname
