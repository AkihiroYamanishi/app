from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

app = Flask(__name__)

# チャネルアクセストークンとチャネルシークレットを設定する
YOUR_CHANNEL_ACCESS_TOKEN = "c8f10886ce5d465a8948b85daf56a168"
YOUR_CHANNEL_SECRET = "lHM1G3h54yfPos/iBAidDmsSSOAibMN7FpwXG285jWrinDeKC5/cQnoOWG7trZ5lbbeyTB3kp9jdVr8hy8fXlwWr23xuC0FhMQtVLiBkflYf8HiHI+WA4SFUcMrAyiSyd1wivwnna6FC4p9NFTdGGQdB04t89/1O/w1cDnyilFU="
line_bot_api = LineBotApi(YOUR_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(YOUR_CHANNEL_SECRET)

# Webhookを受信するエンドポイント
@app.route("/callback", methods=['POST'])
def callback():
    # LINEからのリクエストが正当かどうかをチェックする
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

# Lineから送信されたメッセージを処理する関数
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    if event.message.text == "こんにちは":
        reply_message = "こんにちは！"
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=reply_message))

if __name__ == "__main__":
    app.run()