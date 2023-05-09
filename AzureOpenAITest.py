'''
Notice!!!
python version 3.7.1+
pip install openai == 0.27.0

# Azure OpenAI官方使用文件
https://learn.microsoft.com/zh-tw/azure/cognitive-services/openai/

# 基礎串接使用作法
https://learn.microsoft.com/zh-tw/azure/cognitive-services/openai/quickstart?pivots=programming-language-python&tabs=command-line

# Embedding Model Python串接作法
https://learn.microsoft.com/zh-tw/azure/cognitive-services/openai/tutorials/embeddings?tabs=command-line

# 交談迴圈 (我們今天實測這個)
https://learn.microsoft.com/zh-tw/azure/cognitive-services/openai/how-to/chatgpt?pivots=programming-language-chat-completions

'''

import os
import openai

openai.api_key = "20b3a7765b67455da713a6da0c6703be"
openai.api_base =  "https://skfhopenai1.openai.azure.com/" # your endpoint should look like the following https://YOUR_RESOURCE_NAME.openai.azure.com/
openai.api_type = 'azure'
openai.api_version = '2023-03-15-preview' # this may change in the future

deployment_name='skfhgpt35turbo1' #This will correspond to the custom name you chose for your deployment when you deployed a model.

conversation=[{"role": "system", "content": "You are a helpful assistant."}]

stop = ""
while stop != "掰掰":
    user_input = input('輸入點什麼吧：')
    stop = user_input
    conversation.append({"role": "user", "content": user_input})

    response = openai.ChatCompletion.create(
        engine = deployment_name, # The deployment name you chose when you deployed the ChatGPT or GPT-4 model.
        messages = conversation,
        max_tokens=800,
    )

    conversation.append({"role": "assistant", "content": response['choices'][0]['message']['content']})
    print("\n" + response['choices'][0]['message']['content'] + "\n")