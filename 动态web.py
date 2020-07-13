from flask import Flask
from flask import request,make_response
from pymongo import MongoClient
from json import dumps
import json
from bson import ObjectId
web = Flask(__name__)
client = MongoClient()

class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)
   ###################服务器设置客户端可以跨域访问###################################
from flask_cors import CORS
@web.after_request
def af_request(resp):
    resp = make_response(resp)  ##需要导入一些函数
    resp.headers['Access-Control-Allow-Origin'] = '*'
    resp.headers['Access-Control-Allow-Methods'] = 'GET,POST'
    resp.headers['Access-Control-Allow-Headers'] = 'x-requested-with,content-type'
    return resp
######################################################

CORS(web, supports_credentials=True)


lssx_collection=client["mosoteach_ans"]["lssx1"]
sjjg_collection=client["mosoteach_ans"]["sjjg1"]
def lesson_c(lesson):
    if lesson==1:
        return list(lssx_collection.find())
    elif lesson==2:
        return list(sjjg_collection.find())

def fenhang(collection):
    for ti in collection:
        ti["question"] = ti["question"].replace("\n","")#一些乱码处理
        ti["ans"] = ti["ans"].replace("\n","")
        n=int(len(ti["question"])/25)
        zfc=""
        for i in range(n):
            zfc=zfc+"<xmp>"+ti["question"][25*i:25*(i+1)]+"</xmp>"
        zfc=zfc+"<xmp>"+ti["question"][25*n:]+"</xmp>"
        ti["question"]=zfc
        n=int(len(ti["ans"])/25)
        zfc=""
        for i in range(n):
            zfc=zfc+"<xmp>"+ti["ans"][25*i:25*(i+1)]+"</xmp>"
        zfc=zfc+"<xmp>"+ti["ans"][25*n:]+"</xmp>"
        ti["ans"]=zfc
    return collection
@web.route("/ybk")
def zhuye():
    html=open("index.html","r",encoding="utf-8").read()
    return html
@web.route("/ybklibrary")
def library():
    lesson = int(request.args.get("lesson","1"))
    collection=lesson_c(lesson)
    data=fenhang(collection)
    response_data={"code": 0,"msg":"", "data": data}
    return dumps(response_data,cls=JSONEncoder)
@web.route("/ybk/lssx")
def lssx():
    html=open("lssx.html","r",encoding="utf-8").read()
    return html
@web.route("/ybk/sjjg")
def sjjg():
    html=open("sjjg.html","r",encoding="utf-8").read()
    return html

web.run()
