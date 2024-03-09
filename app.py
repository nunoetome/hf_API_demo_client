import gradio as gr
from gradio_client import Client


DEBUG_MODE = True


def update(name):
    #return f"Welcome to Gradio, {name}!"
    return {"name": name}

def send_request(text):
    client = Client("Nuno-Tome/API_demo_server")
    result = client.predict(
        text,
        api_name="/predict"
    )
    return result

with gr.Blocks() as demo:
    
    with gr.Row():
        gr.Markdown("Start typing below and then click **Run** to see the output.")
        #gr.DuplicateButton()
    with gr.Row():
        with gr.Column():
            gr.Markdown("Type your message:")
            inp = gr.Textbox(placeholder="What is your name?")
        with gr.Column():
          out = gr.JSON()  
    btn = gr.Button("Send request to server")
    btn.click(fn=send_request, inputs=inp, outputs=out)
      
    
        
demo.launch(share=True)