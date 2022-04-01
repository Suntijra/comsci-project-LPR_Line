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

def pushMessageTo_User_On_Line(check_plate,plate_message):
    line_bot_api.push_message(check_plate,TextSendMessage(text=plate_message+' in'))