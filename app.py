#コマンドプロンプトで以下を入力すると開ける
#cd パス
#streamlit run app.py
#ｃｔｒｌ＋ｃでコマンドプロンプト終了

import streamlit as st
from PIL import Image
from bert_score import score



st.title('山アプリ')
st.caption('これは実験用のものです')
st.subheader('自己紹介')
st.text('こんにちは')

pip install -q evaluate
import evaluate

with st.form(key='profile_form'):
    #form開始
    #スライドイメージの入力
    slide_image = st.text_input('スライドのイメージを記入してください')

    #ボタン
    submit_btn = st.form_submit_button('送信')
    cancel_btn = st.form_submit_button('キャンセル')

    #キャンセルか送信で分ける
    if submit_btn:
        st.text(f'「{slide_image}」で作成しました！')
        #モデルの設定    
        bertscore = evaluate.load("bertscore")
        #スライドイメージマスタデータファイルを開く
        with open("/content/drive/MyDrive/Pytorch実装用コード/吾輩は猫である.txt") as f:
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
        for i in range(3):
            #best3を出力
            st.text(f'〇{best_score[i][1]}')
            #print(best_score[i][1][0:3],)
            #画像を出力
            image_ = Image.open(f'{best_score[i][1][0:3]}.jpg')
            st.image(image, width=200)

