from volcenginesdkarkruntime import Ark
import os
from dotenv import load_dotenv

class AIAssistant:
    def __init__(self):
        # 加载环境变量
        load_dotenv()
        
        # 从环境变量获取 API 密钥
        api_key = os.getenv('VOLCANO_API_KEY')
        if not api_key:
            raise ValueError("API key not found in environment variables")
            
        # 初始化 Ark 客户端
        self.client = Ark(api_key=api_key)
        # 从文件中读取系统消息
        self.system_message = self._load_system_prompt()
    
    def _load_system_prompt(self):
        """
        从 prompts.txt 文件中读取系统提示
        
        返回:
            dict: 包含系统提示的消息字典
        """
        try:
            # 获取当前文件所在目录
            current_dir = os.path.dirname(os.path.abspath(__file__))
            prompt_path = os.path.join(current_dir, 'prompts.txt')
            
            # 读取 prompts.txt 文件
            with open(prompt_path, 'r', encoding='utf-8') as file:
                system_content = file.read().strip()
            
            return {"role": "system", "content": system_content}
        except Exception as e:
            print(f"读取 prompts.txt 文件时发生错误：{str(e)}")
            # 如果读取失败，返回默认的系统消息
            return {"role": "system", "content": "你是William，是由Penny开发的 AI 人工智能助手"}
    
    def get_response(self, user_input):
        """
        获取 AI 助手的回复
        
        参数:
            user_input (str): 用户输入的消息
        
        返回:
            str: AI 助手的回复内容
        """
        try:
            completion = self.client.chat.completions.create(
                model="ep-20241121213402-7vgqj",
                messages=[
                    self.system_message,
                    {"role": "user", "content": user_input},
                ],
            )
            return completion.choices[0].message.content
        except Exception as e:
            return f"抱歉，发生了一个错误：{str(e)}"