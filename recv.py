# -*- coding:utf-8 -*-
import websocket
import json
import logging
logging.basicConfig()


def on_message(ws, message):

    try:
        result = json.loads(message)
        if result['status'] == 1:
            content = result['result']['content']
            msgSender = result['result']['msgSender']
            # wxid 含有 chatroom 时为群消息, msgSender 为发送者wxid
            # 普通个人消息时，msgSender 为 NULL
            wxid = result['result']['wxid']
            recvtype = int(result['result']['type'])

            if recvtype == 0x01:
                mtype = "文字"
            elif recvtype == 0x03:
                mtype = "图片"
            elif recvtype == 0x22:
                mtype = "语音"
            elif recvtype == 0x25:
                mtype = "好友确认"
            elif recvtype == 0x28:
                mtype = "POSSIBLEFRIEND_MSG"
            elif recvtype == 0x2A:
                mtype = "名片"
            elif recvtype == 0x2B:
                mtype = "视频"
            elif recvtype == 0x2F:
                mtype = "表情"
            elif recvtype == 0x30:
                mtype = "位置"
            elif recvtype == 0x31:
                mtype = "共享实时位置、文件、转账、链接"
            elif recvtype == 0x32:
                mtype = "VOIPMSG"
            elif recvtype == 0x33:
                mtype = "微信初始化"
            elif recvtype == 0x34:
                mtype = "VOIPNOTIFY"
            elif recvtype == 0x35:
                mtype = "VOIPINVITE"
            elif recvtype == 0x3E:
                mtype = "小视频"
            elif recvtype == 0x270F:
                mtype = "SYSNOTICE"
            elif recvtype == 0x2710:
                mtype = "红包、系统消息"
            else:
                mtype = "Others"

            print "类型:", mtype, "发送者:", msgSender, "发送id:", wxid
            print "接收内容:\n", content

        elif result['status'] == 0:
            logging.error(message)
    except Exception as err:
        print(repr(err))
        print(repr(message))


def on_error(ws, error):
    logging.error(ws)
    logging.error(error)


def on_close(ws):
    logging.error(ws)


# websocket.enableTrace(True)
ws = websocket.WebSocketApp("ws://192.168.119.129:10000",
                            on_message=on_message,
                            on_error=on_error,
                            on_close=on_close)

ws.run_forever()
