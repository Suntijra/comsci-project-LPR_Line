from  linebot_lpr import config
import json
from typing import Text
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,FollowEvent
)
line_bot_api = LineBotApi(config.Channel_access_token)

from pymongo import MongoClient
client = MongoClient('mongodb://santi:Santi!12321@157.245.59.56:27018/?authSource=admin&readPreference=primary&appname=MongoDB%20Compass&directConnection=true&ssl=false')
mydb = client['LPR']['timestamp']

def pushMessageTo_User_On_Line(userid,plate,check):
    query = {
        'plate':plate
    }

    result = mydb.find_one(query)
    print('check ===>>',result)
    txt = 'เลขทะเบียน '+plate
    if check == 'in':
        line_bot_api.push_message(userid,TextSendMessage(text=txt+'\nเวลาเข้า : '+result['DMY']+' '+ result['time']))
    elif check == 'out':
        line_bot_api.push_message(userid,TextSendMessage(text=txt+'\nเวลาออก : '+result['DMY']+' '+ result['time']))
