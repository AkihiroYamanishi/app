#コマンドプロンプトで以下を入力すると開ける
#cd パス
#streamlit run app.py
#ｃｔｒｌ＋ｃでコマンドプロンプト終了

import streamlit as st
from PIL import Image

st.title('山アプリ')
st.caption('これは実験用のものです')
st.subheader('自己紹介')
st.text('こんにちは')

#画像
image = Image.open('./Shohei_Ohtani_(52251755266)_(cropped).jpg')
st.image(image, width=200)


with st.form(key='profile_form'):
    #動画
    #video_file = open('https://www.youtube.com/watch?v=mmK_gRbb2lQ')
    #video_bytes = video_file.read()
    #st.video(video_bytes)

    #テキストボックス
    name = st.text_input('名前')
    #画面がリロードされると値が入ってくるが、カーソルがテキストボックスから外れるとリロードされる


    #ボタン
    submit_btn = st.form_submit_button('送信')
    cancel_btn = st.form_submit_button('キャンセル')

    #キャンセルか送信で分ける
    if submit_btn:
        st.text(f'ようこそ!{name}さん！')
