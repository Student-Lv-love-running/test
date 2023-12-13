import streamlit as st

# 自定义样式
def local_css(file_name):
    with open(file_name, "r", encoding="utf-8") as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# 主界面逻辑
def main():
    local_css('style.css')
    local_css('sidebar_style.css')

if __name__ == "__main__":
    main()
    st.title("Welcome to our Data Visualization Platform!")
