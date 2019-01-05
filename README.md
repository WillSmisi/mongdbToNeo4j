# MongdbToNeo4j
##### 说明：将爬虫的数据导入到neo4j数据库中，follow和fan的关系都变成双向friendship

### 示例图
![demo](https://github.com/WillSmisi/mongdbToNeo4j/blob/master/viewPic/demo.png)



### 主要节点类型
#### 1.Saying:Just like weibo
##### 参数说明：
###### 1.source:来源
###### 2.text:内容
###### 3.picture:图片链接
#### 2.appPerson:User Node
##### 参数说明：
###### 1.avatar:头像地址
###### 2.name:昵称
###### 3.gender(m/f):性别
###### 4.userID:用户标识
###### 5.description:用户个性签名

### Main Relationships
#### Friendship:
##### 参数说明：
###### 1.created_at:建立时间
#### SUBMIT
##### 参数说明：
###### 1.created_at:建立时间
