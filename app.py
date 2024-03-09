import gradio as gr
from gradio_client import Client


DEBUG_MODE = True


def update(name):
    #return f"Welcome to Gradio, {name}!"
    return {"name": name}



with gr.Blocks() as demo:
    
    with gr.Row():
        gr.Markdown("Start typing below and then click **Run** to see the output.")
        #gr.DuplicateButton()
    with gr.Row():
        with gr.Col():
            gr.Markdown("Type your message:")
            inp = gr.Textbox(placeholder="What is your name?")
        with gr.Col():
          out = gr.JSON()  
    btn = gr.Button("Send request to server")
    btn.click(fn=update, inputs=inp, outputs=out)
            
    #with gr.Row():
        #inp = gr.Textbox(placeholder="What is your name?")
        #out = gr.JSON()
        #out = gr.Textbox()
    #btn = gr.Button("Run")
    #btn.click(fn=update, inputs=inp, outputs=out    
    
    
        
demo.launch(share=True)