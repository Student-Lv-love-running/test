import streamlit as st
import os
import pandas as pd
import matplotlib.pyplot as plt

# 设置上传文件的保存目录
UPLOAD_DIRECTORY = "./uploaded_files"
if not os.path.exists(UPLOAD_DIRECTORY):
    os.makedirs(UPLOAD_DIRECTORY)

def save_uploaded_file(uploaded_file):
    """将上传的文件保存到指定目录"""
    if uploaded_file is not None:
        file_path = os.path.join(UPLOAD_DIRECTORY, uploaded_file.name)
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        return file_path
    return None

def upload_page():
    st.title("文件上传")
    uploaded_file = st.file_uploader("选择一个文件", type=None)
    if uploaded_file is not None:
        file_path = save_uploaded_file(uploaded_file)
        if file_path:
            st.success(f"文件 {uploaded_file.name} 已成功上传到服务器！")
        else:
            st.error("文件上传失败。")

def list_files(directory):
    """列出目录中的所有文件并返回它们"""
    files = []
    for filename in os.listdir(directory):
        path = os.path.join(directory, filename)
        if os.path.isfile(path):
            files.append(filename)
    return files

def delete_file(filename):
    """删除指定的文件"""
    file_path = os.path.join(UPLOAD_DIRECTORY, filename)
    if os.path.exists(file_path):
        os.remove(file_path)
        return True
    return False

def plot_bar_chart(df):
    # 确保 DataFrame 有足够的列来绘制柱状图
    if df.shape[1] < 2:
        st.error("CSV 文件至少需要包含两列数据来绘制柱状图。")
        return
    
    # 使用 DataFrame 的第一列作为 X 轴，第二列作为 Y 轴
    x = df.iloc[:, 0]
    y = df.iloc[:, 1]
    
    # 创建柱状图
    plt.figure(figsize=(10, 4))
    bars = plt.bar(x, y, color=plt.cm.get_cmap('tab20', len(x))(range(len(x))))
    
    # 为每个柱子添加标签
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval, round(yval, 2), ha='center', va='bottom')

    # 显示图表
    st.pyplot(plt)

def view_files_page():
    st.title("已上传的文件")
    files = list_files(UPLOAD_DIRECTORY)
    if files:
        selected_file = st.selectbox("选择一个文件来查看内容", files)
        if st.button(f"删除 {selected_file}"):
            if delete_file(selected_file):
                st.success(f"文件 {selected_file} 已删除")
                st.experimental_rerun()
            else:
                st.error(f"文件 {selected_file} 删除失败")
        
         # 添加下载按钮
        with open(os.path.join(UPLOAD_DIRECTORY, selected_file), "rb") as file:
            btn = st.download_button(
                label="下载文件",
                data=file,
                file_name=selected_file,
                mime="text/csv" if selected_file.endswith('.csv') else "application/octet-stream"
            )

        if selected_file.endswith('.csv'):
            df = pd.read_csv(os.path.join(UPLOAD_DIRECTORY, selected_file))
            st.write(df)
            # 调用绘制柱状图的函数
            # plot_bar_chart(df)
        else:
            st.info("选中的文件不是CSV格式，无法显示内容。")
    else:
        st.write("上传目录中没有文件。")

upload_page()
view_files_page()
