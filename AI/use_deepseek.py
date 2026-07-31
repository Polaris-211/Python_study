import os
from openai import OpenAI

#创建客户端对象 DEEPSEEK_API_KEY：环境变量名，值为api——key
client = OpenAI(api_key=os.environ.get('DEEPSEEK_API_KEY'),base_url="https://api.deepseek.com")

#与大模型交互
response = client.chat.completions.create(
    model="deepseek-v4-pro",
    messages=[
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": "How can you do for me"},
    ],
    stream=False,
    reasoning_effort="high",
    extra_body={"thinking": {"type": "enabled"}}
)
# 输出大模型返回的结果
print(response.choices[0].message.content)