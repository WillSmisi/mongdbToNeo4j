from pymongo import MongoClient
from connectNeo4j.pythonNeo4j import CreatFriendShip,creatPersonNode,creatSaying
import json

conn = MongoClient('127.0.0.1', 27017)
db = conn.Sina

#先建立用户节点，再利用构建的ID_Set进行朋友圈的建立
#利用微博中的userID针对ID_SET进行过滤,添加导入

ID_POOL_LIST = []

#对用户相关属性进行过滤操作
users_set = db.users


#遍历创建用户节点
def InputCreateNode():
    userNodeCount = 1;
    for i in users_set.find():
        #删除相关元素
        try:
            i.pop("fans_count","404")
        except KeyError:
            pass
        try:
            i.pop("follows_count","404")
        except KeyError:
            pass
        try:
            i.pop("weibos_count","404")
        except KeyError:
            pass
        try:
            i.pop("cover","404")
        except KeyError:
            pass
        try:
            i.pop("verified","404")
        except KeyError:
            pass
        try:
            i.pop("verified_reason","404")
        except KeyError:
            pass
        try:
            i.pop("follows","404")
        except KeyError:
            pass
        try:
            i.pop('fans',"404")
        except KeyError:
            pass

        try:
            i.pop("verified_reason","404")
        except KeyError:
            pass
        try:
            i.pop("verified_type","404")
        except KeyError:
            pass
        #将清洗后的用户字典作为参数传进去
        #print("创建第",userNodeCount,"个用户节点")
        userNodeCount =userNodeCount+1
        creatPersonNode(i)
        ID_POOL_LIST.append(i['_id'])
    return userNodeCount


#遍历所有用乎中的fans和follows 如果在ID池中，就创建好友关系
def InputFriendShip(ID_POOL_SET):
    friendShipCount = 1;
    for user in users_set.find():
        print("input")
        try:
            if len(user["fans"]):
                fans = user["fans"]
                for fan in fans:
                    if fan["_id"] in ID_POOL_SET:
                        print("创建第",friendShipCount,"个关系")
                        friendShipCount = friendShipCount +1
                        CreatFriendShip(user["_id"],fan["_id"],time="2018-01-05")
        except KeyError:
            pass
        try:
            if len(user["follows"]):
                follows = user["follows"]
                for follow in follows:
                    if follow["_id"] in ID_POOL_SET:
                        print
                        #print("创建第",friendShipCount,"个关系")
                        #friendShipCount = friendShipCount +1
                        CreatFriendShip(user["_id"],follow["_id"],time="2018-01-05")
        except KeyError:
            pass
    return friendShipCount

#遍历所有的微博文档，如果他的用户在ID池中创建微博节点，并且创建关系
def InputWeibo(ID_POOL_SET):
    weiboCount = 1;
    weibo_set = db.weibos

    for weibo in weibo_set.find():
        # 删除相关元素
        try:
            weibo.pop("attitudes_count", "404")
        except KeyError:
            pass

        try:
            weibo.pop("comments_count", "404")
        except KeyError:
            pass
        try:
            weibo.pop("thumbnail", "404")
        except KeyError:
            pass
        try:
            weibo.pop("pictures", "404")
        except KeyError:
            pass
        try:
            weibo.pop("raw_text", "404")
        except KeyError:
            pass
        if weibo["user"] in ID_POOL_SET:
            #添加该微博节点及关系
            print("创建第",weiboCount,"个微博")
            weiboCount = weiboCount+1
            creatSaying(weibo)
    return weiboCount













#对微博相关属性进行过滤操作







if __name__ == "__main__":
    #先创建用户节点

    user=InputCreateNode()
    ID_POOL_SET = set(ID_POOL_LIST)
    print("ID_list长度",len(ID_POOL_LIST))
    
    #创建朋友关系
    friends=InputFriendShip(ID_POOL_SET)
    #创建微博
    weibo=InputWeibo(ID_POOL_SET)
    print ('共创建人数：',user,"关系数",friends,"微博数",weibo)

    '''
    test = []
    test.append("1")
    test.append("2")
    test.append("1")
    testSet =set(test)
    if "1" in testSet:
        print("对的")
    if "1232231" in testSet:
        print("错的")
    '''