# from dotenv import load_dotenv
# load_dotenv()
import streamlit as st
from langchain.chat_models import ChatOpenAI

chat_model = ChatOpenAI()
#st.balloons()
st.title('용수에게 물어봐')

content = st.text_input('묻고싶은 내용을 입력하세요')
st.text('원하는 답변이 아니면 답해줘 버튼을 다시 눌러주세요^^')
# result = chat_model.predict(content + "국악가사를 써줘")
# print(result)

if st.button("답해줘"):
   with st.spinner('작성중...'):
      result = chat_model.predict(content+'작성해줘')
      st.write(result) 
st.image('https://blog.kakaocdn.net/dn/Jz4rd/btsznA1Dj8V/6a8fJWK8KXNTINatD5BFDk/img.jpg')
st.link_button("조용수에대해 좀더 알고 싶으신가요?", "https://m.ntok.go.kr/Changgeuk/Member/Details?Id=79")