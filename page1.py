import streamlit as st
import pandas as pd
st.write("### 你好呀!!!")
st.title("俺的个人网站😃")
st.image("./图片1.webp",width = 200 )

df = pd.DataFrame({"学号":["01","02","03","04","05","06"],
              "班级":["二班","三班","四班","五班","六班","二班"],
              "成绩":[92,51,45,75,86,56]
              })
st.dataframe(df)
st.divider()
st.table(df)