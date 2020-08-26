from pymongo import MongoClient
client = MongoClient(host="127.0.0.1",port=27017)

data0={"_id":0,"title":"某鱼资讯爬虫","secondTitle":"某个实战案例，因需求方取消，只爬取了部分","msg":'''网站有封号反爬虫，并且需求方要求从爬取到的文章中提取出关键日期，而且结果必须以Excel文档保存。<br>是一个综合性非常不错的爬虫案例<br>百度云提取码：hblx''',"pName":"jian_yu_P.PNG","baiDunYun":"https://pan.baidu.com/s/1azbJSNm9hYjIli7sp3AQuA"}
data1={"_id":1,"title":"验证码图片爬取标识","secondTitle":"老师要用机器学习来破解验证码","msg":'''我们自己写代码来获取某车商的验证码，然后用labelme进行标注<br>最后传给老师机器学习，不过因为我们没标注完，所以也没得到成品<br>图片总计有十万张以上，但现在只保留了图片链接<br>百度云提取码：hblx''',"pName":"iCar_P.PNG","baiDunYun":"https://pan.baidu.com/s/1_cyLs7GydJ3C5XF_lWLj6w"}
data2={"_id":2,"title":"Vue框架饿了么后台模拟初认","secondTitle":"为了更深入了解爬虫，我们认识了html5和vue脚手架","msg":'''我们抽出一些时间来更深入的了解html5<br>制作出了一些静态页面和现在的这个网站，不过现在这个网站是动态的了<br>最终我们用Vue做了个粗糙的饿了么后台模拟''',"pName":"vue_P.png","baiDunYun":"none"}
thelist=[data0,data1,data2]
col = client['learn_helper']["learnList"]
returnList=[]
results=col.find({"_id":{"$gte":0}})
for result in results:
    returnList.append(result)
print(returnList)

                                        