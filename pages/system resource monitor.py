import streamlit as st
import os
import pandas as pd
import psutil
import matplotlib.pyplot as plt

# plt.rcParams['font.sans-serif'] = ['DejaVu Sans']  # 设置中文字体为黑体
# plt.rcParams['axes.unicode_minus'] = False  # 正确显示负号

def system_monitor_page():
    st.title("系统资源监控")
    st.markdown("<br><br>", unsafe_allow_html=True) 
    
    if st.button('刷新资源使用情况'):
        st.experimental_rerun()

    st.markdown("<br>", unsafe_allow_html=True) 
        
    col1, space, col2 = st.columns([5,1,5])

    with col1:
        st.subheader("CPU使用率")
        cpu_percent = psutil.cpu_percent(interval=1, percpu=True)
        fig, ax = plt.subplots()
        ax.plot(cpu_percent, marker='o')
        ax.set_xlabel('CPU Cores')
        ax.set_ylabel('Usage Ratio (%)')
        ax.set_title('CPU Usage Ratio')
        ax.spines['right'].set_visible(False)
        ax.spines['top'].set_visible(False)
        ax.set_xticks(range(len(cpu_percent)))
        ax.set_xticklabels([f'c{i}' for i in range(len(cpu_percent))])
        for i, val in enumerate(cpu_percent):
            ax.text(i, val, f"{val:.2f}%", ha='center', va='bottom')
        st.pyplot(fig)
        
    with col2:
        st.subheader("RAM使用情况")
        memory = psutil.virtual_memory()
        fig1, ax1 = plt.subplots()
        # plt.figure(figsize=(10, 8))  # 可以调整图形大小
        ax1.pie([memory.used, memory.total - memory.used], labels=['Used', 'Unused'], autopct='%1.1f%%', startangle=90)
        ax1.axis('equal')
        plt.title('RAM Usage Status')
        st.pyplot(fig1)
    
    st.markdown("<br>", unsafe_allow_html=True) 
    col3, space2, col4 = st.columns([5,1,5])
    with col3:
        st.subheader("磁盘IO")
        # 这里获取磁盘IO数据，并使用适当的图表显示
        # 例如，使用psutil.disk_io_counters()来获取IO信息
        disk_io = psutil.disk_io_counters()
        fig, ax = plt.subplots()
        ax.spines['right'].set_visible(False)
        ax.spines['top'].set_visible(False)
        # 假设disk_io.read_bytes和disk_io.write_bytes包含了需要展示的数据
        io_data = [disk_io.read_bytes, disk_io.write_bytes]
        ax.bar(['Read', 'Write'], io_data)
        ax.set_title('Disk IO')
        # 在这里添加其他你需要的matplotlib的代码来美化图表
        st.pyplot(fig)

    if st.button('刷新使用情况'):
        st.experimental_rerun()

def local_css(file_name):
    with open(file_name, "r", encoding="utf-8") as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

local_css('style.css')
local_css('sidebar_style.css')

system_monitor_page()