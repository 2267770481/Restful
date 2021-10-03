# Restful
这是一个研究restful的工程。    
【说明】    
    由于模型类在每个应用中都是一样的，所以所有的模型类都自demo1中。    
【目录结构如下】    
  apps    
    -demo0: 不使用restful库的情况下设计restful分格接口    
    -demo1: 使用restframework库，展示DRF强大的功能（只需要简单的配置就可以完成增删改查）    
    -demo2: 自定义序列化器与反序列化器    
【请求路由】    
  GET /demoX/books：返回所有book数据    
  POST /demoX/books：新建一条book数据（上传文件）    
  GET /demoX/books/pk：获取某个指定的book数据    
  PUT /demoX/books/pk：更新某个指定的book数据（提供该books的全部信息）    
  PATCH /demoX/books/pk：更新某个指定的book数据（提供该books的部分信息）    
  DELETE /demoX/books/pk：删除某个数据    
