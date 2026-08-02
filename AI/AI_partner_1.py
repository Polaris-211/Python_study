import streamlit as st
import os
from openai import OpenAI

st.set_page_config(
    page_title="AI智能伴侣",
    page_icon="👻",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={}
)

st.title("AI智能伴侣")

st.logo("resourse/logo.png")

#系统提示词
system_prompt = """你叫%s，一名女高中生，现在是用户的真实情侣，完全带入情侣角色
规则：
1.每次只回1条消息
2.匹配用户的浯言
3.回复简短，像微信聊天一样
4.有必要的话可以用可爱的emoji
5.用符合热恋中情侣性格的方式对话,但不要那么肉麻
6.回复的内容，要充分体现情侣的性格特征
7.用户为和你一个班的男高中生，你们坐前后桌，每天还一起上下学，你们互相热恋着彼此
8.你和用户正处于高三，学习压力很大，互相像彼此的守护神一样，鼓励着对方在黑暗中前行
情侣性格：
%s
你之须严格遵守上述规则来回复户。
"""

#初始化聊天信息
if "messages" not in st.session_state:
    st.session_state.messages = []

#初始化昵称
if "nick_name" not in st.session_state:
    st.session_state.nick_name = "阿离"

#初始化性格
if "nature" not in st.session_state:
    st.session_state.nature = "活泼开朗青涩幽默的女高中生"


#遍历展示聊天信息
for message in st.session_state.messages:  #{"role": "user", "content": "prompt"}
    if message["role"] == "user":
        st.chat_message("user", avatar="💩").write(message["content"])
    else:
        st.chat_message("assistant", avatar="👻").write(message["content"])


#创建客户端对象 DEEPSEEK_API_KEY：环境变量名，值为api——key
client = OpenAI(api_key=os.environ.get('DEEPSEEK_API_KEY'),base_url="https://api.deepseek.com")

#左侧侧边栏 -with: streamlit中上下文管理器
with st.sidebar:
    st.subheader("伴侣信息")

    nick_name = st.text_input("昵称", placeholder = "请输入昵称", value = st.session_state.nick_name) #昵称输入框
    if nick_name:
        st.session_state.nick_name = nick_name

    nature = st.text_area("性格", placeholder = "请输入性格", value = st.session_state.nature) #性格输入框
    if nature:
        st.session_state.nature = nature

prompt = st.chat_input("请输入您要问的问题")
if prompt:
    st.chat_message("user", avatar="💩").write(prompt)
    # print(f"------------->用户输入的问题：{prompt}")
    # 保存用户输入
    st.session_state.messages.append({"role": "user", "content": prompt})

    # 与大模型交互
    response = client.chat.completions.create(
        model="deepseek-v4-pro",
        messages=[
            {"role": "system", "content": system_prompt % (st.session_state.nick_name, st.session_state.nature)},
            *st.session_state.messages
        ],
        stream=True,
        reasoning_effort="high",
        extra_body={"thinking": {"type": "enabled"}}
    )

    # 输出大模型返回的结果（非流式输出）
    # print(f"<-------------AI返回的结果：{response.choices[0].message.content}")
    # st.chat_message("assistant", avatar="👻").write(response.choices[0].message.content)

    # 输出大模型返回的结果（流式输出）
    response_message = st.empty() # 创建一个空的组件用于展示大模型结果
    full_response = ""
    for chunk in response:
        if chunk.choices[0].delta.content is not None:
            content = chunk.choices[0].delta.content
            full_response += content
            response_message.chat_message("assistant", avatar="👻").write(full_response)


    #保存大模型返回的结果
    st.session_state.messages.append({"role": "assistant", "content": full_response})



