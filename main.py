import streamlit as st

from utills import generate_script
st.title("视频脚本一键生成器")


with st.sidebar:
    key=st.text_input("输入密钥，限DS",type="password")
    st.markdown("[获取DS密钥](https://platform.deepseek.com/usage)")
subject=st.text_input("请输入视频的主题")
video_length=st.number_input("请输入视频的时长：",min_value=0.1,step=0.1)
creativity=st.slider("请输入视频脚本的创造力，调整模型温度，越高创造了越高",min_value=0.1,max_value=2.0,value=1.0,step=0.1)
submit=st.button("一键生成")

if submit and not key:
    st.info("请检查密钥是否输入")
    st.stop()
if submit and not subject:
    st.info("请输入视频主题")
    st.stop()
if submit:
    with st.spinner("耐心等待ing...."):
        title,scripy,search_result=generate_script(subject,video_length,creativity,key)
    st.success("视频脚本以生产")
    st.write(title)
    st.subheader("视频脚本")
    st.write(scripy)

    with st.expander("这里是维基百科"):
        st.info(search_result)




