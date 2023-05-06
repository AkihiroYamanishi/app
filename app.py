#コマンドプロンプトで以下を入力すると開ける
#cd パス
#streamlit run app.py
#ｃｔｒｌ＋ｃでコマンドプロンプト終了
#pip install git+https://github.com/huggingface/evaluate.git

import streamlit as st

#from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import requests
import json
#from flask import Flask, request, abort
import openai
import os
import re
#import requests
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)


st.set_page_config(
    page_title="スライド検索アプリ", 
    #page_icon=image, 
    layout="wide", 
    initial_sidebar_state="auto", 
    )

# Line Developersサイトで取得したChannel Access TokenとChannel Secret
YOUR_CHANNEL_ACCESS_TOKEN = 'lHM1G3h54yfPos/iBAidDmsSSOAibMN7FpwXG285jWrinDeKC5/cQnoOWG7trZ5lbbeyTB3kp9jdVr8hy8fXlwWr23xuC0FhMQtVLiBkflYf8HiHI+WA4SFUcMrAyiSyd1wivwnna6FC4p9NFTdGGQdB04t89/1O/w1cDnyilFU='
YOUR_CHANNEL_SECRET = 'c8f10886ce5d465a8948b85daf56a168'

# Line Messaging APIのURL
#line_api_url = 'https://api.line.me/v2/bot/message/reply'

line_bot_api = LineBotApi(YOUR_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(YOUR_CHANNEL_SECRET)

# OpenAI APIの設定を行います
openai.api_key = "YOUR_OPENAI_API_KEY"
model_engine = "text-davinci-002"

# メッセージを受信したときに呼び出される関数
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    # ユーザーから受信したメッセージを取得します
    received_message = event.message.text

    # ユーザーから受信したメッセージをOpenAIに送信して、応答を取得します
    response = openai.Completion.create(
        engine=model_engine,
        prompt=received_message,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7
    )

    # OpenAIから受信した応答を取得します
    message_text = response.choices[0].text.strip()

    # ユーザーに応答を送信します
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=message_text)
    )

# LINE Messaging APIからのWebhook URLを受信するエンドポイント
@app.route("/callback", methods=["POST"])
def callback():
    signature = request.headers["X-Line-Signature"]
    body = request.get_data(as_text=True)
    try:
        handler.handle(body, signature)
    return 'OK'





# Hugging Face Transformersライブラリで使用するモデルとトークナイザー
#model_name = 'facebook/bart-large-cnn'
#tokenizer = AutoTokenizer.from_pretrained(model_name)
#model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

#from PIL import Image
#import os
#from bert_score import score
#import evaluate
#from evaluate import load
#image = Image.open(f'./picture/{best_score[i][1][0:5]}.jpg')
#st.image(image, width=600)

#st.title('山アプリ')
#st.caption('これは実験用のものです')
#st.subheader('自己紹介')
#st.text('こんにちは')
#pip install -q evaluate
#install evaluate

###slide_image = st.radio(label='フォーマットを選択してください',options=('01_プロセス','02_並列','03_比較','04_ロジックツリー','05_マトリックス', '06_棒グラフ', '07_散布図', '08_折れ線グラフ', '09_滝グラフ','10_複合グラフ'),index=0,horizontal=True,)
#スライドイメージで選択した画像を一つ表示
###image = Image.open(f'./picture/{slide_image}/01.jpg')
###st.image(image, use_column_width=True)

###with st.form(key='profile_form'):
    #form開始
    #スライドイメージの入力
    #slide_image = st.text_input('スライドのイメージを記入してください')
    #選択肢をもっと増やす
    #slide_image1 = st.selectbox('フェーズ', ['背景・現状','課題','施策検討','今後の方針','分析'], index=0)
    #slide_image2 = st.selectbox('スライドの型', ['','表＿施策カバー範囲','表＿矢印','表＿グラフ','表＿箇条書き','ロジックツリー（原因の分解）','海外状況','散布図','事業分野企業ごと','折れ線グラフ','滝グラフ','棒グラフ＿トレンド','棒グラフ＿強調','棒グラフ＿補足情報','棒グラフ×折れ線グラフ','サイクル','サプライチェーン','スキーム','スキルジャーニー','ヒアリング結果','マトリクス','マトリクス＿方向','ロードマップ'], index=0)
    #slide_image = slide_image1 + slide_image2
    # index=0 なので初期値は ０番目のもの が表示される。
    #st.text(slide_image)
    #ボタン
    ###submit_btn = st.form_submit_button('フォーマット例表示')
    ###cancel_btn = st.form_submit_button('キャンセル')
    #キャンセルか送信で分ける
    ###if submit_btn:
        ###st.text(f'「{slide_image}」のスライド例を表示')
        #モデルの設定    
        #bertscore = evaluate.load("bertscore")
        #スライドイメージマスタデータファイルを開く
        #with open("./picture//text.txt") as f:
        #    list = [line.strip() for line in f]
        #モデルの設定
        #model = 'roberta-base'
        #スコアリストの作成
        #ls_score_pred = []
        #スライドイメージとマスタデータの類似度点数づけ
        #for data in list:
            #score_pred = bertscore.compute(predictions=[slide_image], references=[data],model_type=model,lang="ja")['f1'][0]
            #ls_score_pred.append([score_pred, data])
            #best_score = sorted(ls_score_pred,reverse=True)
        #フォルダの中のファイル数を確認
        ###dir = f'./picture/{slide_image}'
        ###count_file = sum(os.path.isfile(os.path.join(dir,name)) for name in os.listdir(dir))
        #ベスト5を表示
        ###for i in range(count_file):
            #best3を出力
            #st.text(f'〇{best_score[i][1]}')
            #print(best_score[i][1][0:3],)
            #画像を出力
           ### if i == 6:
           ###     break
           ### st.subheader(f'{i+1}番目のスライド例')
           ### image = Image.open(f'./picture/{slide_image}/0{i+1}.jpg')
           ### st.image(image, use_column_width=True)

#出典を明記
###st.text('出典：「https://www.meti.go.jp/meti_lib/report/H30FY/000141.pdf」ボストンコンサルティンググループ')
###st.text('出典：「https://www.meti.go.jp/shingikai/mono_info_service/digital_jinzai/jissenteki_manabi_wg/pdf/001_03_02.pdf」ボストンコンサルティンググループ')
###st.text('出典：「https://www.meti.go.jp/shingikai/enecho/shigen_nenryo/sekiyu_gas/pdf/001_04_00.pdf」マッキンゼーアンドカンパニー')
###st.text('出典：「https://www.mhlw.go.jp/file/05-Shingikai-12201000-Shakaiengokyokushougaihokenfukushibu-Kikakuka/sorupi5.pdf」マッキンゼーアンドカンパニー')
###st.text('出典：「https://www.meti.go.jp/shingikai/mono_info_service/textile_industry/pdf/001_06_00.pdf」ローランドベルガー')
###st.text('出典：「https://www.meti.go.jp/committee/kenkyukai/energy_environment/sekiyu_seisei/pdf/001_06_00.pdf」ローランドベルガー')
###st.text('出典：「https://www.meti.go.jp/shingikai/mono_info_service/new_cvs/pdf/004_02_00.pdf」A.T.カーニー')
###st.text('出典：「https://www.meti.go.jp/shingikai/mono_info_service/smart_mobility_challenge/pdf/20190408_04.pdf」アーサー・ディ・リトル・ジャパン')
###st.text('出典：「https://www.meti.go.jp/press/2020/09/20200928002/20200928002-2.pdf」アーサー・ディ・リトル・ジャパン')
###st.text('出典：「https://www.meti.go.jp/policy/investment/pdf/2021tainichi_chosa.pdf」アクセンチュア')
###st.text('出典：「https://www.meti.go.jp/meti_lib/report/2020FY/000668.pdf」アクセンチュア')
