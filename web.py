from flask import Flask
from flask import request,make_response
from flask import render_template
from datetime import timedelta
from pymongo import MongoClient
from json import dumps
import re
import json
from bson import ObjectId
from flask import jsonify

web = Flask(__name__)
web.config['SEND_FILE_MAX_AGE_DEFAULT'] = timedelta(seconds=30)

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
def lesson_c(lesson,ti):
    returnList=[]
    if len(ti)>0:
        if int(lesson)==1:
            for u in lssx_collection.find({'question':re.compile(ti)}):
                returnList.append(u)
        elif int(lesson)==2:
            for u in sjjg_collection.find({'question':re.compile(ti)}):
                returnList.append(u)
    #print('长度'+str(len(ti)))
    if len(returnList)==0:
        returnList=[{'_id': '1', 'question': '抱歉找不到这道题\n', 'correct_ans': '--', 'ans': '--\n'}]
    return returnList

@web.route("/")
def zhuye():
    return render_template('index.html')
@web.route("/list")
def xueXiList():
    return render_template('learnList.html')
@web.route("/ybk")
def ti_lib():
    return render_template('ti_lib.html')
@web.route("/ybklibrary",methods=["POST"])
def library():
    postForm=json.loads(request.get_data(as_text=True))
    '''对于前端POST请求发送过来的json数据，Flask后台可使用 request.get_data() 来接收数据，
    数据的格式为 bytes；加上as_text=True 参数后就变成 Unicode 了； 
    再使用 json.loads() 方法就可以转换字典。'''
    #print(postForm)
    lesson=postForm["lesson"]
    ti=postForm["ti"]
    collection=lesson_c(lesson,ti)

    response_data={"code": 0,"msg":"", "data": collection}
    return dumps(response_data,cls=JSONEncoder)
@web.route("/listmsg")
def xueXiListMsg():
    collection=client["learn_helper"]["learnList"]
    results=collection.find({"_id":{"$gte":0}})
    returnList=[]
    for result in results:
        returnList.append(result)
    response_data={"code": 0,"msg":"", "data": returnList}
    #return jsonify({"data":returnList})也可以使用
    return dumps(response_data,cls=JSONEncoder)


#web.run(host="0.0.0.0",port=80)#运行服务器
web.run()




