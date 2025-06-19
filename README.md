# 🧠 Real-Time Chatbot using Groq + Python
This is a **terminal-based AI chatbot** built with Python using **Groq’s LLaMA 3 (70B)** model. It streams responses in real-time and can be customized for different use cases and personalities.

## 📸 Demo


## 🚀 Features
* Powered by Groq's LLaMA 3 (70B)  
* Real-time streaming responses  
* Simple CLI interface  
* Customizable chatbot behavior   
* Uses .env for secure API key storage  

## 📦 Requirements
* Python 3.8+  
* Groq API Key  
* groq Python SDK  
* python-dotenv (for .env support)  

## 🔧 Installation
**1. Clone this repo / download the file**  
**2.Install dependencies**  
pip install groq python-dotenv  
**3.Create a .env file in the same directory:**  
GROQ_API_KEY=your_groq_api_key_here  
**4.Run the chatbot**   
python main.py  

## ✨ Customization
You can modify the chatbot’s tone and behavior by editing the system message:  

{"role": "system", "content": "You are a helpful and witty chatbot."}  

## 📄 License
This project is open-source and free to use under the MIT License.

## 🙌 Credits
Built with 💙 using [Groq](https://groq.com/) + [LLaMA 3](https://www.llama.com/) Inspired by the simplicity of CLI + the power of large language models.
