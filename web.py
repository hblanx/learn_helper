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
def fanye(lesson):
    if(lesson==1):
        ans_list=list(lssx_collection.find())
        lesson_name="离散数学"
    elif(lesson==2):
        ans_list=list(sjjg_collection.find())
        lesson_name="数据结构"
    else:
        return("无此课程")
    html='''
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>学校考试题</title>
<style type="text/css">
    h1{margin:0px auto;
    width:70%;}
    h2{margin:0px auto;
    width:70%;}
</style>
</head>
<body>
<h1>使用方法：CTRL+F进行搜索</h1>
<h2>当前课程：
'''
    html=html+lesson_name+"</h2>"
    for ti in ans_list:
        ti["question"] = ti["question"].replace("\n","")
        ti["ans"] = ti["ans"].replace("\n","")
        html=html+"<xmp>"+ti["question"]+" "+ti["ans"]+"</xmp>正确答案："+ti["correct_ans"]+"<br>"
    html=html+'''
</body>
</html>'''
    return html#这里显示语法错误，但是可以运行
@web.route("/ybk")
def shuchu():#定义输出函数，注意此函数在@web的下面
    lesson = int(request.args.get("lesson","1"))#获得page请求
    #limit = int(request.args.get("limit","20"))#同上，但1和20需要修改成输入的内容，因为我的任务不详，我就没做了
    return str(fanye(lesson))#返回（打印）的内容
#注意：此处的地址不同于以往需要http://127.0.0.1:5000/Server/Captcha_Web_Page/1?page=1&limit=2
#web.run()
web.run(host="0.0.0.0",port=80)#运行服务器
