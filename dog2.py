#! /usr/bin/env  python
#coding=utf-8
import itchat,json,os
# tuling plugin can be get here:
# https://github.com/littlecodersh/EasierLife/tree/master/Plugins/Tuling
from tuling import get_response
from ramdonChoicePic import getRanPic
from NetEaseMusicApi import interact_select_song

HELP_MSG = u'''\
欢迎使用微信网易云音乐
帮助： 显示帮助
关闭： 关闭歌曲
歌名： 按照引导播放音乐\
'''

with open('stop.mp3', 'w') as f: pass
def close_music():
    os.startfile('stop.mp3')

@itchat.msg_register('Text')
def text_reply(msg):
    if msg['ToUserName'] == 'filehelper':
        if msg['Text'] == u'关闭':
            close_music()
            itchat.send(u'音乐已关闭', 'filehelper')
        if msg['Text'] == u'帮助':
            itchat.send(HELP_MSG, 'filehelper')
        else:
            itchat.send(interact_select_song(msg['Text']), 'filehelper')
    else:
        if u'作者' in msg['Text'] or u'主人' in msg['Text']:
            return u'Jack Yang'
        elif u'获取图片' in msg['Text']:
            itchat.send('@img@aa.gif', msg['FromUserName']) # there should be a picture
        elif u'每日一图' in msg['Text']:
            fileName, description = getRanPic("aa")
            img_msg= '@img@%s' % fileName
            itchat.send(img_msg, msg['FromUserName']) # there should be a picture
            return description
        else:
            print msg['Text']
            return get_response(msg['Text']) or u'收到：' + msg['Text']

@itchat.msg_register(['Picture', 'Recording', 'Attachment', 'Video'])
def atta_reply(msg):
    return ({ 'Picture': u'图片', 'Recording': u'录音',
        'Attachment': u'附件', 'Video': u'视频', }.get(msg['Type']) +
        u'已下载到本地') # download function is: msg['Text'](msg['FileName'])

@itchat.msg_register(['Map', 'Card', 'Note', 'Sharing'])
def mm_reply(msg):
    if msg['Type'] == 'Map':
        return u'收到位置分享'
    elif msg['Type'] == 'Sharing':
        return u'收到分享' + msg['Text']
    elif msg['Type'] == 'Note':
        return u'收到：' + msg['Text']
    elif msg['Type'] == 'Card':
        return u'收到好友信息：' + msg['Text']['Alias']

@itchat.msg_register('Text', isGroupChat = True)
def group_reply(msg):
    if msg['isAt']:
        #print json.dumps(msg, indent = 4)
        if u'每日一图' in msg['Text']:
            fileName, description = getRanPic("aa")
            img_msg= '@img@%s' % fileName
            itchat.send(img_msg, msg['FromUserName']) # there should be a picture
            return description
        else:
            text =  msg['Text'][msg['Text'].find(u'\u2005')+1:]
            print text
            return u'@%s\u2005%s' % (msg['ActualNickName'],
                get_response(text) or u'收到：' + msg['Text'])

@itchat.msg_register('Friends')
def add_friend(msg):
    itchat.add_friend(**msg['Text'])
    itchat.send_msg(u'Hello there!', msg['RecommendInfo']['UserName'])

itchat.auto_login(True, enableCmdQR=2)
itchat.run()
