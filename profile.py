import streamlit as st
from PIL import Image

st.title("Profile")
"Streamlitを使って簡単なProfile作成してみました。"

st.write("名前：駆け出しエンジニア")
st.write("年齢：27歳")
st.write("出身：愛知県")
st.write("趣味：野球")

img = Image.open("77683391.jpg")
st.image(img)
st.write("・某アパレル会社のアルバイトを２年→新卒入社。")
st.write("・コロナの影響や、収入面、環境の変化によりIT業界へ転職。")
st.write("・現在はJavaの現場で稼働し、Python習得中（Django,Flask,AI領域）")


expander = st.expander("スキル")
expander.write("Java１年６ヶ月~(現在SES稼働中)")
expander.write("Python")
expander.write("HTML")
expander.write("CSS")

st.write("※streamlitは本来こういうProfile作成には向いていないです。")
st.write("どういうものが作れるのか。という感じで作ったのでデザインや機能は普遍ですね。。笑")
st.write("ただし！話題にもなっているということで、気になる方は勉強して損はないと思います！！！")
