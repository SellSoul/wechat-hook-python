# -*- coding:utf-8 -*-
import requests
import json
import logging

logging.basicConfig()

HOST, PORT = "192.168.119.129", 10000


# 好友功能
def sendMsg(wxid, msg):
    """
    参数 wxid, msg
    发送消息
    msg Success
    """
    url = "http://" + str(HOST) + ":" + str(PORT) + "/api/msg/sendtextmsg"
    try:
        datamsg = {"wxid": wxid, "msg": msg}
        req = requests.post(url, data=datamsg, timeout=5)
        result = json.loads(req.content)
        status = result['status']
        if status == 1:
            return result['result']
        elif status == 0:
            logging.error(result['result'])
            return None
        else:
            return None
    except Exception as err:
        logging.error(err)
        return None


def sendFile(wxid, filepath):
    """
    参数 wxid, filepath
    发送消息
    msg Success
    """
    url = "http://" + str(HOST) + ":" + str(PORT) + "/api/msg/sendfilemsg"
    try:
        datamsg = {"wxid": wxid, "filepath": filepath}
        req = requests.post(url, data=datamsg, timeout=5)
        result = json.loads(req.content)
        status = result['status']
        if status == 1:
            return result['result']
        elif status == 0:
            logging.error(result['result'])
            return None
        else:
            return None
    except Exception as err:
        logging.error(err)
        return None


def sendImage(wxid, imgpath):
    """
    参数 wxid, imgpath
    发送消息
    msg Success
    """
    url = "http://" + str(HOST) + ":" + str(PORT) + "/api/msg/sendimgmsg"
    try:
        datamsg = {"wxid": wxid, "imgpath": imgpath}
        req = requests.post(url, data=datamsg, timeout=5)
        result = json.loads(req.content)
        status = result['status']
        if status == 1:
            return result['result']
        elif status == 0:
            logging.error(result['result'])
            return None
        else:
            return None
    except Exception as err:
        logging.error(err)
        return None


def sendCardMsg(receverWxid, sendWxid, nickName):
    """
    参数 receverWxid, sendWxid, nickName
    发送名片
    msg Success
    """
    url = "http://" + str(HOST) + ":" + str(PORT) + "/api/msg/sendcardmsg"
    try:
        datamsg = {"receverWxid": receverWxid, "sendWxid": sendWxid, "nickName": nickName}
        req = requests.post(url, data=datamsg, timeout=5)
        result = json.loads(req.content)
        status = result['status']
        if status == 1:
            return result['result']
        elif status == 0:
            logging.error(result['result'])
            return None
        else:
            return None
    except Exception as err:
        logging.error(err)
        return None


def addUser(wxid, msg):
    """
    参数 wxid, msg
    添加好友
    msg Success
    """
    url = "http://" + str(HOST) + ":" + str(PORT) + "/api/user/adduser"
    try:
        datamsg = {"msg": msg, "wxid": wxid}
        req = requests.post(url, data=datamsg, timeout=5)
        result = json.loads(req.content)
        status = result['status']
        if status == 1:
            return result['result']
        elif status == 0:
            logging.error(result['result'])
            return None
        else:
            return None
    except Exception as err:
        logging.error(err)
        return None


def delUser(wxid):
    """
    参数 wxid
    删除好友
    msg Success
    """
    url = "http://" + str(HOST) + ":" + str(PORT) + "/api/user/deluser"
    try:
        datamsg = {"wxid": wxid}
        req = requests.post(url, data=datamsg, timeout=5)
        result = json.loads(req.content)
        status = result['status']
        if status == 1:
            return result['result']
        elif status == 0:
            logging.error(result['result'])
            return None
        else:
            return None
    except Exception as err:
        logging.error(err)
        return None


# 获取列表功能
def getUserList():
    """
    参数 None
    返回好友、群、公粽号信息 类型:字典
    备注 remark
    账号 account
    头像 avatar
    wxid wxid
    昵称 nickname
    """
    url = "http://" + str(HOST) + ":" + str(PORT) + "/api/user/getuserlist"
    try:
        req = requests.get(url, timeout=5)
        result = json.loads(req.content)
        status = result['status']
        if status == 1:
            temp = json.loads(result['result']['msg'])
            return temp
        elif status == 0:
            logging.error(result['result'])
            return None
        else:
            return None
    except Exception as err:
        logging.error(err)
        return False


def getRoomUserList(roomid):
    """
    参数 roomid
    返回群成员信息 类型:字典
    群 roomid
    群好友 wxid, ^G 分割
    群主 wxid
    """
    url = "http://" + str(HOST) + ":" + str(PORT) + "/api/group/getuserlist"
    try:
        datamsg = {"roomid": roomid}
        req = requests.post(url, data=datamsg, timeout=20)
        result = json.loads(req.content)
        status = result['status']
        if status == 1:
            temp = json.loads(result['result']['msg'])[0]
            return temp
        elif status == 0:
            logging.error(result['result'])
            return None
        else:
            return None
    except Exception as err:
        logging.error(err)
        return None


def getAllRoomUserList():
    """
    参数 None
    返回所有群信息 类型:列表
    群 roomid
    群好友 wxid, ^G 分割
    群主 wxid
    """
    url = "http://" + str(HOST) + ":" + str(PORT) + "/api/group/getalluserlist"
    try:
        req = requests.get(url, timeout=20)
        result = json.loads(req.content)
        status = result['status']
        if status == 1:
            temp = json.loads(result['result']['msg'])
            return temp
        elif status == 0:
            logging.error(result['result'])
            return None
        else:
            return None
    except Exception as err:
        logging.error(err)
        return None


# 群功能
def setRoomAnnouncement(roomid, announcement):
    """
    参数 roomid, announcement
    设置群公告
    msg Success
    """
    url = "http://" + str(HOST) + ":" + str(PORT) + "/api/group/setroomannouncement"
    try:
        datamsg = {"roomid": roomid, "announcement": announcement}
        req = requests.post(url, data=datamsg, timeout=5)
        result = json.loads(req.content)
        status = result['status']
        if status == 1:
            return result['result']
        elif status == 0:
            logging.error(result['result'])
            return None
        else:
            return None
    except Exception as err:
        logging.error(err)
        return None


def sendRoomAtMsg(roomid, wxid, nickname, msg):
    """
    参数 roomid, wxid, nickname, msg
    发送群@消息
    msg Success
    """
    url = "http://" + str(HOST) + ":" + str(PORT) + "/api/group/sendatmsg"
    try:
        datamsg = {"roomid": roomid, "wxid": wxid, "nickname": nickname, "msg": msg}
        req = requests.post(url, data=datamsg, timeout=5)
        result = json.loads(req.content)
        status = result['status']
        if status == 1:
            return result['result']
        elif status == 0:
            logging.error(result['result'])
            return None
        else:
            return None
    except Exception as err:
        logging.error(err)
        return None


def delRoomUser(roomid, wxid):
    """
    参数 roomid, wxid
    删除群好友
    msg Success
    """
    url = "http://" + str(HOST) + ":" + str(PORT) + "/api/group/deluser"
    try:
        datamsg = {"roomid": roomid, "wxid": wxid}
        req = requests.post(url, data=datamsg, timeout=5)
        result = json.loads(req.content)
        status = result['status']
        if status == 1:
            return result['result']
        elif status == 0:
            logging.error(result['result'])
            return None
        else:
            return None
    except Exception as err:
        logging.error(err)
        return None


def addRoomUser(roomid, wxid):
    """
    参数 roomid, wxid
    添加好友至群
    msg Success
    """
    url = "http://" + str(HOST) + ":" + str(PORT) + "/api/group/adduser"
    try:
        datamsg = {"roomid": roomid, "wxid": wxid}
        req = requests.post(url, data=datamsg, timeout=5)
        result = json.loads(req.content)
        status = result['status']
        if status == 1:
            return result['result']
        elif status == 0:
            logging.error(result['result'])
            return None
        else:
            return None
    except Exception as err:
        logging.error(err)
        return None


def getUserInfo(wxid):
    """
    参数 wxid
    获取群好友信息
    msg Success
    """
    url = "http://" + str(HOST) + ":" + str(PORT) + "/api/group/userinfo"
    try:
        datamsg = {"wxid": wxid}
        req = requests.post(url, data=datamsg, timeout=5)
        result = json.loads(req.content)
        status = result['status']
        if status == 1:
            return json.loads(result['result']['msg'])[0]
        elif status == 0:
            logging.error(result['result'])
            return None
        else:
            return None
    except Exception as err:
        logging.error(err)
        return None


def editGroupName(roomid, roomname):
    """
    参数 roomid, roomname
    修改群名称
    msg Success
    """
    url = "http://" + str(HOST) + ":" + str(PORT) + "/api/group/editname"
    try:
        datamsg = {"roomid": roomid, "roomname": roomname}
        req = requests.post(url, data=datamsg, timeout=5)
        result = json.loads(req.content)
        status = result['status']
        if status == 1:
            return json.loads(result['result']['msg'])[0]
        elif status == 0:
            logging.error(result['result'])
            return None
        else:
            return None
    except Exception as err:
        logging.error(err)
        return None


def quitGroup(roomid):
    """
    参数 roomid
    退出群
    msg Success
    """
    url = "http://" + str(HOST) + ":" + str(PORT) + "/api/group/quitgroup"
    try:
        datamsg = {"roomid": roomid}
        req = requests.post(url, data=datamsg, timeout=5)
        result = json.loads(req.content)
        status = result['status']
        if status == 1:
            return json.loads(result['result']['msg'])[0]
        elif status == 0:
            logging.error(result['result'])
            return None
        else:
            return None
    except Exception as err:
        logging.error(err)
        return None

