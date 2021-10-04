#这是一个研究restful的工程。 
####使用过程中有问题或扩展一定要看docs/下边的DRF资料。
##序列化器作用:
    1, 序列化: 将模型类对象, 转成json(dict)数据
    2, 反序列化: 将json(dict)数据, 转成模型类对象
    ①: 校验
    ②: 入库
        ①: 校验
            1, 字段类型校验
            2, 字段选项校验
            3, 单字段校验, 方法  def validate_字段名(self, attrs):
            4, 多字段校验, 方法  def validate(self, attrs):
            5, 自定义校验, 方法  自己写检验函数，在定义字段的时候用validators=[函数名]引入  
###【说明】    
      由于模型类在每个应用中都是一样的，所以所有的模型类都自demo1中。    
###【目录结构如下】    
    apps    
      -demo0: 不使用restful库的情况下设计restful分格接口    
      -demo1: 使用restframework库，展示DRF强大的功能（只需要简单的配置就可以完成增删改查）    
      -demo2: 自定义序列化器与反序列化器    
###【请求路由】    
    GET /demoX/books：返回所有book数据    
    POST /demoX/books：新建一条book数据（上传文件）    
    GET /demoX/books/pk：获取某个指定的book数据    
    PUT /demoX/books/pk：更新某个指定的book数据（提供该books的全部信息）    
    PATCH /demoX/books/pk：更新某个指定的book数据（提供该books的部分信息）    
    DELETE /demoX/books/pk：删除某个数据    
    GET /docs/: 接口文档