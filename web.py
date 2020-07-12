from flask import Flask
from flask import request
from pymongo import MongoClient
#from json import dumps

'''内容不用学部分(运行不了)
import json
from bson import OBJectId
class JSONEncoder(json.JSONEncoder):
    def default(self,o):
        if isinstance(o,ObjectId):
            return str(o)
        return json.JSONEncoder.default(self,o)
'''
web = Flask(__name__)
client = MongoClient()
lssx_collection=client["mosoteach_ans"]["lssx1"]
sjjg_collection=client["mosoteach_ans"]["sjjg1"]
lesson=1
html=""
def html_maker():
    html='''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!--标准开头-->
    <title>题库查询</title>
    <link rel="stylesheet" href="/static/bootstrap.min.css">
</head>
<body>
    <ul class="nav nav-pills">
        <li role="presentation" class="active"><a href="/static/index.html">主页</a></li>
        <li role="presentation"><a href="/static/sjjg.html">数据结构</a></li>
        <li role="presentation"><a href="#">离散数学</a></li>
    </ul>
    <div class="alert alert-success alert-dismissible" role="alert">
        <button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button>
        <strong>成功！</strong> 登陆服务器
      </div>
    <p>这里是主页</p>
</body>
<script src="/static/jquery-3.5.1.min.js"></script>
<script src="/static/bootstrap.min.js"></script>
</html>
'''
    return html
@web.route("/ybk")
def shuchu():#定义输出函数，注意此函数在@web的下面
    #lesson = int(request.args.get("lesson","1"))获得page请求
    return str(html_maker())

#web.run()
web.run(host="0.0.0.0",port=80)#运行服务器
