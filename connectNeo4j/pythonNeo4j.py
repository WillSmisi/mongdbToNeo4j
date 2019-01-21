import py2neo
from py2neo import Graph,Node,Relationship,NodeMatcher

graph = Graph(
    "bolt://112.74.36.158:7687",
    username="neo4j",
    password="123456"
)
print(py2neo.__version__)
#节点和关系命名配置
personNodeName = "Person"
weiboRelationshipName = "Release"
friendshipName = "Friend"
weiboNodeName = "Dynamic"

#创建用户节点
def creatPersonNode(userDict):
    tempNode = Node(personNodeName,userid=userDict["_id"])
    for (key ,value) in userDict.items():
        if key == '_id':
            pass
        else:
            tempNode[key] = value
    return graph.create(tempNode)


#根据ID获取用户节点
def getPersonNode(id):
    matcher = NodeMatcher(graph)
    retNode = matcher.match(personNodeName,userid=id).first()
    return retNode

#包括创建一个微博和关系,前提该微博的用户ID已存在图中
def creatSaying(sayingDict):
    tempNode = Node(weiboNodeName,contents=sayingDict["contents"])
    userNode=getPersonNode(sayingDict["user"])
    for (key ,value) in sayingDict.items():
        if key in ['text','created_at','user','_id','reposts_count']:
            pass
        else:
            tempNode[key] = value
    graph.create(tempNode)
    submit = Relationship(userNode, weiboRelationshipName,tempNode,create_Date=sayingDict['created_at'])
    return graph.create(submit)


#之前应该做一个字典关系的判断，字典mapping朋友关系，已创建就不必再创建了
def CreatFriendShip(AuserId,BuserID,time):
    aUserNode = getPersonNode(AuserId)
    bUserNode = getPersonNode(BuserID)
    friendshipA = Relationship(aUserNode, friendshipName, bUserNode, created_at=time)
    friendshipB = Relationship(bUserNode, friendshipName, aUserNode, created_at=time)
    graph.create(friendshipA)
    graph.create(friendshipB)

############测试建立好友关系#####
'''# 结果：成功

aNode = {"_id": "5646958853", "avatar": "https://tva4.sinaimg.cn/crop.0.0.80.80.180/006aa3Xvjw8etr1vd9z0bj3028028q2p.jpg", "cover": "https://tva1.sinaimg.cn/crop.0.0.640.640.640/549d0121tw1egm1kjly3jj20hs0hsq4f.jpg", "description": "", "gender": "m", "name": "\u675c\u80b2\u660e"}
bNode = {"_id": "2721313097", "avatar": "https://tva2.sinaimg.cn/crop.0.0.1080.1080.180/a233f149jw8ex6oknprm1j20u00u0tcg.jpg", "cover": "https://tva3.sinaimg.cn/crop.0.0.640.640.640/a1d3feabjw1eca1ktsx9tj20hs0hsjtk.jpg", "description": "", "gender": "f", "name": "LEAUQEAAN"}
creatPersonNode(aNode)
creatPersonNode(bNode)
CreatFriendShip("5646958853","2721313097","2018-01-05")
'''



###################测试微博，建立发布关系
'''
testWeibo={ "user": "2721313097"  ,"created_at": "01-02", "picture": "http://wx1.sinaimg.cn/large/8f1fe6aaly1fysak97abzj20zk0f4759.jpg",  "source": "\u4e13\u4e1a\u7248\u5fae\u535a", "text": "\u611f\u8c22\u5927\u5bb6\u966a\u6211\u4eec\u8d70\u8fc7\u4eae\u70b9\u9887\u591a\u7684 2018\uff0c\u65b0\u4e00\u5e74\u7684\u8d77\u70b9\uff0c\u8bf7\u5927\u5bb6\u4ee5 &quot;\u5f00\u53d1&quot; \u4e3a\u4e3b\u9898\uff0c\u5728\u5fae\u4fe1\u7559\u8a00\u4e2d\u5199\u51fa 2018 \u5e74\u5bf9\u60a8\u5f71\u54cd\u6700\u5927\u3001\u611f\u89e6\u6700\u6df1\u7684 Google \u6280\u672f\u6216\u670d\u52a1\uff0c\u5e76\u8bf4\u660e\u7406\u7531\u3002\u6211\u4eec\u4f1a\u4e3a\u83b7\u5f97\u70b9\u8d5e\u6570\u6700\u591a\u7684 3 \u4f4d\u670b\u53cb\u9001\u4e0a\u597d\u793c\u3002\u70b9\u51fb\u94fe\u63a5\u56de\u987e 2018 \u5e76\u53c2\u4e0e\u6d3b\u52a8\uff01  <a data-url=\"http://t.cn/EbDKZeN\" target=\"_blank\" href=\"https://weibo.cn/sinaurl/blocked76bd2b21?url=https%3A%2F%2Fmp.weixin.qq.com%2Fs%3F__biz%3DMzAwODY4OTk2Mg%3D%3D%26mid%3D2652048064%26idx%3D1%26sn%3D168456e5ad91b01ab7d0d1d021e8891c&share_menu=1&sinainternalbrowser=topnav&mid=4324042960357382&luicode=10000011&lfid=1076032401232554&u=https%3A%2F%2Fmp.weixin.qq.com%2Fs%3F__biz%3DMzAwODY4OTk2Mg%3D%3D%26mid%3D2652048064%26idx%3D1%26sn%3D168456e5ad91b01ab7d0d1d021e8891c\" class=\"\"><span class='url-icon'><img style='width: 1rem;height: 1rem' src='https://h5.sinaimg.cn/upload/2015/09/25/3/timeline_card_small_web_default.png'></span><span class=\"surl-text\">\u518d\u89c1\uff0c2018\uff01\u4f60\u597d\uff0c2019\uff01</span></a> "}
creatSaying(testWeibo)
'''


'''
tempNode = Node("Test",userID=testDict['_id'])
tx = graph.begin()
tx.create(tempNode)
tx.commit()
'''


#print(test_graph.create(test_node_1))
'''

from py2neo import NodeMatcher

matcher = NodeMatcher(graph)
matcher.match("Test").first()
'''