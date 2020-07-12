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
def fenhang(html,ans_list):
    for ti in ans_list:
        ti["question"] = ti["question"].replace("\n","")#一些乱码处理
        ti["ans"] = ti["ans"].replace("\n","")
        if len(ti["question"])>=125:
            html=html+"<tr><td><xmp>"+ti["question"][0:35]+"</xmp><xmp>"
            html=html+ti["question"][35:70]+"</xmp><xmp>"
            html=html+ti["question"][70:95]+"</xmp><xmp>"
            html=html+ti["question"][95:120]+"</xmp><xmp>"
            html=html+ti["question"][120:]+"</xmp></td>" 
        elif len(ti["question"])>=95:
            html=html+"<tr><td><xmp>"+ti["question"][0:35]+"</xmp><xmp>"
            html=html+ti["question"][35:70]+"</xmp><xmp>"
            html=html+ti["question"][70:95]+"</xmp><xmp>"
            html=html+ti["question"][95:]+"</xmp></td>"              
        elif len(ti["question"])>=75:
            html=html+"<tr><td><xmp>"+ti["question"][0:35]+"</xmp><xmp>"
            html=html+ti["question"][35:70]+"</xmp><xmp>"
            html=html+ti["question"][70:]+"</xmp></td>"        
        elif len(ti["question"])>=30:
            html=html+"<tr><td><xmp>"+ti["question"][0:35]+"</xmp><xmp>"+ti["question"][35:]+"</xmp></td>"
    
        else:
            html=html+"<tr><td><xmp>"+ti["question"]+"</xmp></td>"
                
        if len(ti["ans"])>=95:
            html=html+"<td><xmp>"+ti["ans"][0:35]+"</xmp><xmp>"
            html=html+ti["ans"][35:70]+"</xmp><xmp>"
            html=html+ti["ans"][70:95]+"</xmp><xmp>"
            html=html+ti["ans"][95:]+"</xmp></td>"             
        elif len(ti["ans"])>=75:
            html=html+"<td><xmp>"+ti["ans"][0:35]+"</xmp><xmp>"
            html=html+ti["ans"][35:70]+"</xmp><xmp>"
            html=html+ti["ans"][70:]+"</xmp></td>"        
        elif len(ti["ans"])>=30:
            html=html+"<td><xmp>"+ti["ans"][0:35]+"</xmp><xmp>"+ti["ans"][35:]+"</xmp></td>"
        else:
            html=html+"<td><xmp>"+ti["ans"]+"</xmp></td>"
        html=html+"<td id='ans'>"+ti["correct_ans"]+"<td></tr>\n"
    return html

@web.route("/ybk")
def shuchuybk():#主页
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
<body style="background-color:#EFFEFE">
    <ul class="nav nav-pills">
        <li role="presentation" class="active"><a href="/ybk">主页</a></li>
        <li role="presentation"><a href="/ybk/sjjg">数据结构</a></li>
        <li role="presentation"><a href="/ybk/lssx">离散数学</a></li>
    </ul>
    <div class="alert alert-success alert-dismissible" role="alert">
        <button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button>
        <strong>成功！</strong> 登陆服务器
      </div>
    <p>这里是主页</br>
    项目的github主页
    <a href="https://github.com/hblanx/learn_helper.git"target="_blank">点击传送</a>
    </p>
</body>
<script src="/static/jquery-3.5.1.min.js"></script>
<script src="/static/bootstrap.min.js"></script>
</html>
'''
    return html
@web.route("/ybk/sjjg")
def shuchusjjg():
    html='''
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!--标准开头-->
    <title>题库查询</title>
    <link rel="stylesheet" href="/static/bootstrap.min.css">
    <style type="text/css">
        #ans{
            font-size: 28px;
            color: #ff4500;
        }
    </style>
</head>
<body>
    <ul class="nav nav-pills">
        <li role="presentation"><a href="/ybk">主页</a></li>
        <li role="presentation" class="active"><a href="/ybk/sjjg">数据结构</a></li>
        <li role="presentation"><a href="/ybk/lssx">离散数学</a></li>
    </ul>
    <div class="panel panel-default">
        <div class="panel-heading">这里是数据结构</div>
        <div class="panel-body">
          <p>使用CTRl+F进行搜索</p>
        </div>
      
        <table class="table">
            <thead>
                <tr>
                    <th>题目</th>
                    <th>选项</th>
                    <th>正确答案</th>
                </tr>
            </thead>
            <tbody>'''
    ans_list=list(sjjg_collection.find())
    html=fenhang(html,ans_list)
    html=html+'''            </tbody>
        </table>
      </div>
</body>
<script src="/static/jquery-3.5.1.min.js"></script>
<script src="/static/bootstrap.min.js"></script>
</html>
    '''
    return html

@web.route("/ybk/lssx")
def shuchulssx():
    html='''
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!--标准开头-->
    <title>题库查询</title>
    <link rel="stylesheet" href="/static/bootstrap.min.css">
    <style type="text/css">
        #ans{
            font-size: 28px;
            color: #ff4500;
        }
    </style>
</head>
<body>
    <ul class="nav nav-pills">
        <li role="presentation"><a href="/ybk">主页</a></li>
        <li role="presentation"><a href="/ybk/sjjg">数据结构</a></li>
        <li role="presentation" class="active"><a href="/ybk/lssx">离散数学</a></li>
    </ul>
    <div class="panel panel-default">
        <div class="panel-heading">这里是离散数学</div>
        <div class="panel-body">
          <p>使用CTRl+F进行搜索</p>
        </div>
      
        <table class="table">
            <thead>
                <tr>
                    <th>题目</th>
                    <th>选项</th>
                    <th>正确答案</th>
                </tr>
            </thead>
            <tbody>'''
    ans_list=list(lssx_collection.find())
    html=fenhang(html,ans_list)
    html=html+'''            </tbody>
        </table>
      </div>
</body>
<script src="/static/jquery-3.5.1.min.js"></script>
<script src="/static/bootstrap.min.js"></script>
</html>
    '''
    return html

web.run()
#web.run(host="0.0.0.0",port=80)#运行服务器
