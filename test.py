import streamlit as st
import os

# 设置上传文件的保存目录
UPLOAD_DIRECTORY = "./uploaded_files"

# 如果上传目录不存在，则创建它
if not os.path.exists(UPLOAD_DIRECTORY):
    os.makedirs(UPLOAD_DIRECTORY)

def save_uploaded_file(uploaded_file):
    """将上传的文件保存到指定目录"""
    if uploaded_file is not None:
        file_path = os.path.join(UPLOAD_DIRECTORY, uploaded_file.name)
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        return True
    return False

def main():
    st.title("文件上传示例")

    uploaded_file = st.file_uploader("选择一个文件", type=None)
    if uploaded_file is not None:
        # 文件保存到服务器
        if save_uploaded_file(uploaded_file):
            st.success(f"文件 {uploaded_file.name} 已成功上传到服务器！")
        else:
            st.error("文件上传失败。")

if __name__ == "__main__":
    main()
