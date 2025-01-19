import streamlit as st

with st.sidebar:
    name = st.text_input("请输入你的名字：")
    if name:
        st.write(f"你好,{name}")


columns1,columns2,columns3 = st.columns([2,2,1])
with columns1:
    password = st.text_input("请输入你的密码：", type="password")
    st.divider()
    paragraph = st.text_area("请输入一段自我介绍")

with columns2:
    age = st.number_input("输入你的年龄", value=20, min_value=0, max_value=100, step=1)
    st.write(f"你的年龄是{age}")


with columns3:
    checked = st.checkbox("同意以上条款")

    if checked:
        st.write("感谢您的同意")

    submitted = st.button("提交")
    if submitted:
        st.write("提交成功")








st.divider()


st.divider()

