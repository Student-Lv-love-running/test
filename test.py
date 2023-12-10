import streamlit as st
import os
import pandas as pd

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
        return file_path  # 返回文件的保存路径
    return None

def list_files(directory):
    """列出目录中的所有文件并返回它们"""
    files = []
    for filename in os.listdir(directory):
        path = os.path.join(directory, filename)
        if os.path.isfile(path):
            files.append(filename)
    return files

def main():
    st.title("文件上传")

    uploaded_file = st.file_uploader("选择一个文件", type=None)  # 允许任何类型的文件
    if uploaded_file is not None:
        # 文件保存到服务器
        file_path = save_uploaded_file(uploaded_file)
        if file_path:
            st.success(f"文件 {uploaded_file.name} 已成功上传到服务器！")
            # 如果文件是 CSV 文件，读取并显示
            if uploaded_file.name.endswith('.csv'):
                df = pd.read_csv(file_path)
                st.write(df)
            else:
                st.info("已上传非 CSV 文件，无法显示内容。")
        else:
            st.error("文件上传失败。")

    # 列出已上传的文件
    if st.checkbox("显示已上传的文件"):
        files = list_files(UPLOAD_DIRECTORY)
        if files:
            for f in files:
                with open(os.path.join(UPLOAD_DIRECTORY, f), "rb") as file:
                    st.download_button(label=f"下载 {f}", data=file, file_name=f, mime='application/octet-stream')
        else:
            st.write("上传目录中没有文件。")

if __name__ == "__main__":
    main()
    st.write("tips: 所有类型的文件都能上传，但是只展示csv文件的内容")
