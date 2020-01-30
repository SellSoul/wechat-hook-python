# WeChatAPI
WeChat Hook API


## 发送文字
```python
result = sendMsg("wxid_thisisfortest", "你好")
print(result['msg'])
```

## 发送文件
```python
result = sendFile("wxid_thisisfortest", "c:\\temp.zip")
print(result['msg'])
```

## 发送图片
```python
result = sendImage("wxid_thisisfortest", "c:\\temp.jpg")
print(result['msg'])
```

## 发送名片
```python
result = sendCardMsg("wxid_thisisfortest", "wxid_iopzb6obm66p22", "若惜")
print(result['msg'])
```

## 添加好友
```python
result = addUser("wxid_thisisfortest", "添加好友招呼")
print(result['msg'])
```

## 删除好友
```python
result = delUser("wxid_thisisfortest")
print(result['msg'])
```

## 获取群好友列表功能
```python
temp = getRoomUserList("test@chatroom")
print temp['roomid'], temp['accounts'], temp['roommasterid']
```

## 获取所有群好友列表功能
```python
temp = getAllRoomUserList()
for oneRoom in temp:
    print oneRoom['roommasterid'], oneRoom['roomid'], oneRoom['accounts']
```

## 获取好友列表
```python
temp = getUserList()
for user in temp:
    print user['account'], user['wxid'], user['nickname'], user['remark'], user['avatar']
```

## 群通知功能
```python
result = setRoomAnnouncement("test@chatroom", "群里会自动推送撸羊毛的线报，请自行关注")
print(result['msg'])
```

## 群@消息
```python
temp = getUserList()
for user in temp:
    if user['wxid'] == "wxid_thisisfortest":
        nickname = user['nickname']
        result = sendRoomAtMsg("test@chatroom", "wxid_thisisfortest", nickname, "测试")
        print(result['msg'])
```

## 删除群好友
```python
result = delRoomUser("test@chatroom", "wxid_thisisfortest")
print(result['msg'])
```

## 添加好友至群
```python
result = addRoomUser("test@chatroom", "wxid_thisisfortest")
print(result['msg'])
```

## 获取群好友详细信息
```python
temp = getRoomUserList("test@chatroom")
temp = getAllRoomUserList()
for oneRoom in temp:
    templist = [account for account in oneRoom['accounts'].split("^G") if account != '']
    for wxid in templist:
        result = getUserInfo(wxid)
        print result['wxid'], result['nickname'], result['wxnumber']
```

## 修改群名称
```python
result = editGroupName("test@chatroom", '羊毛裙')
print(result['msg'])
```

## 退出群
```python
result = quitGroup("test@chatroom")
print(result['msg'])
```

联系作者：xiaochao_perish
