from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

app = Flask(__name__)

# チャネルアクセストークンとチャネルシークレットを設定する
YOUR_CHANNEL_ACCESS_TOKEN = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
YOUR_CHANNEL_SECRET = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
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