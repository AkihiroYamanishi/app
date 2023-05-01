#コマンドプロンプトで以下を入力すると開ける
#cd パス
#streamlit run app.py
#ｃｔｒｌ＋ｃでコマンドプロンプト終了
#pip install git+https://github.com/huggingface/evaluate.git

import streamlit as st
from PIL import Image
#from bert_score import score
import evaluate
from evaluate import load
#image = Image.open(f'./picture/{best_score[i][1][0:5]}.jpg')
#st.image(image, width=600)
st.set_page_config(
    page_title="スライド検索アプリ", 
    #page_icon=image, 
    layout="wide", 
    initial_sidebar_state="auto", 
    )
#st.title('山アプリ')
#st.caption('これは実験用のものです')
#st.subheader('自己紹介')
#st.text('こんにちは')

#pip install -q evaluate
#install evaluate

with st.form(key='profile_form'):
    #form開始
    #スライドイメージの入力
    
    #slide_image = st.text_input('スライドのイメージを記入してください')
    #選択肢をもっと増やす
    slide_image = st.selectbox('Select item', ['棒グラフ', '滝グラフ', '課題','表'], index=0)
    # index=0 なので初期値は ０番目のもの が表示される。
    st.text(slide_image)
    #ボタン
    submit_btn = st.form_submit_button('送信')
    cancel_btn = st.form_submit_button('キャンセル')

    #キャンセルか送信で分ける
    if submit_btn:
        st.text(f'「{slide_image}」で検索')
        #モデルの設定    
        bertscore = evaluate.load("bertscore")
        #スライドイメージマスタデータファイルを開く
        with open("./picture/text.txt") as f:
            list = [line.strip() for line in f]
        #モデルの設定
        model = 'roberta-base'
        #スコアリストの作成
        ls_score_pred = []
        #スライドイメージとマスタデータの類似度点数づけ
        for data in list:
            score_pred = bertscore.compute(predictions=[slide_image], references=[data],model_type=model,lang="ja")['f1'][0]
            ls_score_pred.append([score_pred, data])
            best_score = sorted(ls_score_pred,reverse=True)
        #ベスト5を表示
        for i in range(5):
            #best3を出力
            #st.text(f'〇{best_score[i][1]}')
            #print(best_score[i][1][0:3],)
            #画像を出力
            st.subheader(f'{i+1}番目のスライド例')
            image = Image.open(f'./picture/{best_score[i][1][0:5]}.jpg')
            st.image(image, use_column_width=True)

