import os

BASE_DIRS = os.path.dirname(__file__)

#参数
options = {
    "port" : 8002,
}



#配置
settings = {
    "static_path": os.path.join(BASE_DIRS,"static"),
    "template_path":os.path.join(BASE_DIRS,"templates"),
    "debug":True,          #1.自动重启２．取消缓存编译模板３．取消缓存静态文件的ｈａｓｈ值４．提供追踪信息
    #"autoreload": True,     #仅自动重启
}