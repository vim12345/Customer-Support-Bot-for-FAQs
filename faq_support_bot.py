import openai
import os
import gradio as gr
 
# Set your OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")  # or paste your key directly
 
# FAQ knowledge base (optional: load from file)
faq_context = """
FAQs:
Q: What are your business hours?
A: We are open Monday to Friday, 9 AM to 6 PM.
 
Q: How can I reset my password?
A: Click on 'Forgot Password' on the login page and follow the instructions.
 
Q: Where do you ship to?
A: We ship to all 50 U.S. states and select international locations.
 
Q: How can I contact support?
A: Email us at support@example.com or call 1-800-123-4567.
"""
 
def get_faq_response(user_input):
    messages = [
        {"role": "system", "content": "You are a helpful customer support agent. Use the FAQ information below to answer questions as accurately as possible.\n" + faq_context},
        {"role": "user", "content": user_input}
    ]
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error: {str(e)}"
 
# Create a simple Gradio interface
iface = gr.Interface(
    fn=get_faq_response,
    inputs="text",
    outputs="text",
    title="Customer Support FAQ Bot",
    description="Ask any frequently asked question. Example: 'What are your business hours?'"
)
 
iface.launch()