from flask import Flask
from flask import request
from pymongo import MongoClient
from json import dumps
import json
from bson import ObjectId


class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)

web = Flask(__name__)
client = MongoClient()
img_collection=client["mosoteach_ans"]["sjjg1"]
def lesson_c(lesson):
    return list(img_collection.find())#这里显示语法错误，但是可以运行
@web.route("/ybl")
def zhuye():
    html='''
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!--标准开头-->
    <title>题库查询</title>
    <link rel="stylesheet" href="bootstrap.min.css">
    <link href="index.css" rel="stylesheet">
</head>
<body style="background-color:#bbffff">
    <ul class="nav nav-pills">
        <li role="presentation" class="active"><a href="#">主页</a></li>
        <li role="presentation"><a href="#">数据结构</a></li>
        <li role="presentation"><a href="#">离散数学</a></li>
    </ul>
    <div class="alert alert-success alert-dismissible" role="alert">
        <button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button>
        <strong>成功！</strong> 登陆服务器
      </div>
      <hr/>
    <p>这里是主页</p>
</body>
<script src="jquery-3.5.1.min.js"></script>
<script src="bootstrap.min.js"></script>
</html>
    '''
    return html
@web.route("/ybklibrary")
def shuchu():
    lesson = int(request.args.get("lesson","1"))
    data=lesson_c(lesson)
    response_data={"code": 0, "data": data}
    return dumps(response_data,cls=JSONEncoder)

web.run()
