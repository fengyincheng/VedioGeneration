import os

from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_community.utilities import WikipediaAPIWrapper

def generate_script(subject,video_length,
                    creativity,api_key):
    title_template = ChatPromptTemplate.from_messages(
        [
            ("human", "请为'{subject}'这个主题的视频想一个吸引人的标题")

        ]

    )
    scripy_template = ChatPromptTemplate.from_messages(
        [
            ("human",
             """你是一位短视频频道的博主。根据以下标题和相关信息，为短视频频道写一个视频脚本。
             视频标题：{title}，视频时长：{duration}分钟，生成的脚本的长度尽量遵循视频时长的要求。
             要求开头抓住限球，中间提供干货内容，结尾有惊喜，脚本格式也请按照【开头、中间，结尾】分隔。
             整体内容的表达方式要尽量轻松有趣，吸引年轻人。
             脚本内容可以结合以下维基百科搜索出的信息，但仅作为参考，只结合相关的即可，对不相关的进行忽略：
             ```{wikipedia_search}```""")
        ]
    )

    model = ChatOpenAI(
    model="deepseek-chat",             # DeepSeek 的对话模型
    api_key=api_key,                   # 你传进来的 DeepSeek Key
    base_url="https://api.deepseek.com",
    temperature=creativity,
    )


    title_chain= title_template|model
    print("标题生成完成")
    scripy_chain= scripy_template|model
    print("准备访问 Wikipedia")

    title=title_chain.invoke({"subject":subject}).content
    print("Wikipedia 返回了")

    search = WikipediaAPIWrapper(lang="zh")

    try:
        search_result = search.run(subject)
    except Exception:
        search_result="(诶呀，出错了)"

    scripy=scripy_chain.invoke({"title":title,"duration":video_length,
                                "wikipedia_search":search_result}).content
    return title,scripy,search_result

#print(generate_script("猫咪",1,1.0,"sk-c77ab36b39c3440cbed1858c23823d68"))

