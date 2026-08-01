import streamlit as st

st.set_page_config(
    page_title="streamlitr入门",
    page_icon="🌏",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)


st.title("Streamlit Study")
st.header("Streamlit first title")
st.subheader("Streamlit second title")

st.write("知识点：本次作业围绕运动的合成与分解，包含小船渡河、牵连绳速分解")
st.write("19 题（小车联动弹簧斜面）")
st.write("30 题（动滑轮速度、拉力动力学）")
st.write("学习建议：牢记绳端分解核心规则：物体实际速度沿绳、垂直绳分解，沿绳分速度等于绳收缩速率；")

st.image("./resourse/猫.jpg")

st.audio("resourse/刀盾.mp3")

st.video("resourse/意外.mp4")

st.logo("resourse/猫.jpg")

student_data = {
    "姓名": ["王林", "张三", "李四", "王五", "赵六"],
    "学号": ["20260001", "20260002", "20260003", "20260004", "20260005"],
    "语文": [98,90 ,59 ,29 ,80 ],
    "数学": [88, 23, 54, 87, 100],
    "英语": [67, 88, 36, 77, 0],
    "总分": [67, 88, 36, 77, 0],
}
st.table(student_data)



name=st.text_input("昵称")
st.write(f"你的昵称是：{name}")

password =st.text_input("密码", type="password")
st.write(f"你的密码是：{password}")

gender=st.radio("性别",["男","女","未知"], index=2)
st.write(f"你的性别是：{gender}")
































