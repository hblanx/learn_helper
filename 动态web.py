from flask import Flask
from flask import request,make_response
from flask import render_template
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


lssx_collection=client["mosoteach_ans"]["lssx_html"]
sjjg_collection=client["mosoteach_ans"]["sjjg1"]
def lesson_c(lesson):
    if lesson==1:
        return list(lssx_collection.find())
    elif lesson==2:
        return list(sjjg_collection.find())

@web.route("/ybk")
def zhuye():
    return render_template('index.html')
@web.route("/ybklibrary")
def library():
    lesson = int(request.args.get("lesson","1"))
    collection=lesson_c(lesson)
    response_data={"code": 0,"msg":"", "data": collection}
    return dumps(response_data,cls=JSONEncoder)
@web.route("/ybk/lssx")
def lssx():
    return render_template('lssx.html')
@web.route("/ybk/sjjg")
def sjjg():
    return render_template('sjjg.html')

#web.run(host="0.0.0.0",port=80)#运行服务器
web.run()

