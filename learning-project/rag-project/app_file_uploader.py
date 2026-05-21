"""
RAG知识库更新的可视化界面 (Streamlit)
"""
import time

import streamlit as st
from knowledge_base import KnowledgeBaseService

st.title('知识库更新服务')

uploader_file = st.file_uploader(
    "请上传txt文件", # 标题
    type=['txt'], # 支持的文件类型
    accept_multiple_files=False, # 是否允许上传多个文件
)

service = KnowledgeBaseService()

# session_state是streamlit的一个存储状态的字典
if 'service' not in st.session_state:
    st.session_state['service'] = service

if uploader_file is not None:
    file_name = uploader_file.name
    file_type = uploader_file.type
    file_size = uploader_file.size / 1024

    st.subheader(f'文件名：{file_name}')
    st.write(f"格式：{file_type} | 大小：{file_size:.2f} KB")

    # get_value ->  bytes -> decode(utf-8)
    text = uploader_file.getvalue().decode("utf-8")

    with st.spinner('载入知识库中...'):
        time.sleep(1)
        result = st.session_state["service"].upload_by_str(text, file_name)
        st.write(result)