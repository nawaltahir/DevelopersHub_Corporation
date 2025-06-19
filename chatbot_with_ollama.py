import gradio as gr
import requests

# Add a system prompt to guide the model
chat_history = [
    {
        "role": "system",
        "content": "You are a helpful and friendly medical assistant. Answer general health-related questions clearly and safely. Avoid giving any serious medical advice or suggesting medications without disclaimers."
    }
]

def query_ollama(prompt):
    global chat_history
    chat_history.append({"role": "user", "content": prompt})

    response = requests.post(
        "http://localhost:11434/api/chat",
        json={
            "model": "mistral",  # or use "phi" if you're running that
            "messages": chat_history,
            "stream": False  # <- This disables streaming
        }
    )

    if response.status_code == 200:
        reply = response.json()["message"]["content"]
        chat_history.append({"role": "assistant", "content": reply})
        return reply
    else:
        return "Error: Could not connect to the Ollama model."

def reset_chat():
    global chat_history
    chat_history = [
        {
            "role": "system",
            "content": "You are a helpful and friendly medical assistant. Answer general health-related questions clearly and safely. Avoid giving any serious medical advice or suggesting medications without disclaimers."
        }
    ]
    return "", ""

with gr.Blocks() as demo:
    gr.Markdown("## 🩺 General Health Chatbot (Local Mistral via Ollama)")
    chatbot = gr.Chatbot()
    user_input = gr.Textbox(placeholder="Ask a health question...")
    send_btn = gr.Button("Send")
    clear_btn = gr.Button("Clear")

    def respond(message, history):
        reply = query_ollama(message)
        history = history + [[message, reply]]
        return "", history

    send_btn.click(respond, [user_input, chatbot], [user_input, chatbot])
    clear_btn.click(fn=reset_chat, outputs=[user_input, chatbot])

demo.launch()
