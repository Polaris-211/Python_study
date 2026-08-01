import streamlit as st
import os
from openai import OpenAI

st.set_page_config(
    page_title="AI只能伴侣",
    page_icon="👻",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={}
)

st.title("AI只能伴侣")

st.logo("resourse/logo.png")

#系统提示词
system_prompt = "You are a helpful assistant"

#初始化聊天信息
if "messages" not in st.session_state:
    st.session_state.messages = []

#遍历展示聊天信息
for message in st.session_state.messages:  #{"role": "user", "content": "prompt"}
    if message["role"] == "user":
        st.chat_message("user", avatar="💩").write(message["content"])
    else:
        st.chat_message("assistant", avatar="👻").write(message["content"])


#创建客户端对象 DEEPSEEK_API_KEY：环境变量名，值为api——key
client = OpenAI(api_key=os.environ.get('DEEPSEEK_API_KEY'),base_url="https://api.deepseek.com")

prompt = st.chat_input("请输入您要问的问题")
if prompt:
    st.chat_message("user", avatar="💩").write(prompt)
    print(f"------------->用户输入的问题：{prompt}")
    # 保存用户输入
    st.session_state.messages.append({"role": "user", "content": prompt})

    # 与大模型交互
    response = client.chat.completions.create(
        model="deepseek-v4-pro",
        messages=[
            {"role": "system", "content": system_prompt},
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



