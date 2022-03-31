import json
from typing import Text
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,FollowEvent
)
import config
import insert_id_User
app = Flask(__name__)

line_bot_api = LineBotApi(config.Channel_access_token)
handler = WebhookHandler(config.Channel_secret)


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'
#ส่ง message
line_bot_api.push_message('Ufc7556c9f724503aa08f98b62d2cdb9d',TextSendMessage(text='5กธ9147'))
# @handler.add(MessageEvent, message=TextMessage)
# def handle_message():
#     line_bot_api.push_message('Ufc7556c9f724503aa08f98b62d2cdb9d',TextSendMessage(text='5กธ9147'))


# if __name__ == "__main__":
#     app.run()