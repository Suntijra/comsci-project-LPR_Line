import json
from flask import Flask, request, abort

from linebot_lpr import (
    LineBotApi, WebhookHandler
)
from linebot_lpr.exceptions import (
    InvalidSignatureError
)
from linebot_lpr.models import (
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
    jsonData = request.get_json(force=True,silent=True)
    user_id = jsonData['events'][0]['source']['userId']
    #increate insert database
    insert_id_User.insert_id_user_line(user_id)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'
@app.route('')
def home():
    return 'connect'
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    app.run()