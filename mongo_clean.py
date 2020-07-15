from pymongo import MongoClient

client = MongoClient()
#a=client['mosoteach_ans'].list_collection_names()
#print(a)
collection = list(client['mosoteach_ans']['lssx1'].find())
new_collection=client['mosoteach_ans']['lssx_html']
def language(zfc):#检测输入字符串是否合法
    if "<a" in zfc:
        return False
    elif "< a" in zfc:
        return False
    elif "<A" in zfc:
        return False
    elif "< A" in zfc:
        return False
    else:
        return True
for ti in collection:
    ti["question"] = ti["question"].replace("\n","")#一些乱码处理
    ti["ans"] = ti["ans"].replace("\n","")
    if not language(ti["question"]):
        n=int(len(ti["question"])/25)
        zfc=""
        for i in range(n):
            zfc=zfc+"<xmp>"+ti["question"][25*i:25*(i+1)]+"</xmp>"
        zfc=zfc+"<xmp>"+ti["question"][25*n:]+"</xmp>"
        ti["question"]=zfc
    if not language(ti["ans"]):
        n=int(len(ti["ans"])/25)
        zfc=""
        for i in range(n):
            zfc=zfc+"<xmp>"+ti["ans"][25*i:25*(i+1)]+"</xmp>"
        zfc=zfc+"<xmp>"+ti["ans"][25*n:]+"</xmp>"
        ti["ans"]=zfc
    new_collection.insert(ti)