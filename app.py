import streamlit as st
from ai_lw import AIAssistant

def main():
    # 设置页面标题
    st.title("AI 智能助手 - William")
    
    # 初始化会话状态
    if "messages" not in st.session_state:
        st.session_state.messages = []
        
    if "ai_assistant" not in st.session_state:
        st.session_state.ai_assistant = AIAssistant()

    # 显示聊天历史
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # 获取用户输入
    if prompt := st.chat_input("请输入您的问题"):
        # 添加用户消息到历史记录
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # 获取 AI 助手的回复
        with st.chat_message("assistant"):
            # 显示加载动画
            with st.spinner("思考中..."):
                response = st.session_state.ai_assistant.get_response(prompt)
                st.markdown(response)
                
        # 添加助手回复到历史记录
        st.session_state.messages.append({"role": "assistant", "content": response})

if __name__ == "__main__":
    main() 