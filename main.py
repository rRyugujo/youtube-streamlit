import streamlit as st
import time


st.title('Streamlit 超入門')
st.write("プログレスバーの表示")

"Start!!"

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f"Iteration {i+1}")
    bar.progress(i + 1)
    time.sleep(0.1)
    




left_clomus, right_columns = st.columns(2)

button = left_clomus.button("右カラムに文字を表示")
if button:
    right_columns.write("ここは、右カラム")

expander = st.expander("問い合わせ")
expander.write("問い合わせ内容を書く")


#text = st.text_input("あなたの趣味を教えてください。")


#condistion = st.slider("あなたの今の調子は？", 0, 100, 50)


#"あなたの趣味:", text
#"コンディション:", condistion
#if st.checkbox("Show Image")
#    img = Image.open("sample.jpg")
#    st.image(img, caption="皇居", use_column_width=True)

