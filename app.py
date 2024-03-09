import gradio as gr
from gradio_client import Client

client = Client("Nuno-Tome/API_demo_server")
DEBUG_MODE = True


def request(text):

    result = client.predict(
        text,
		api_name="/predict"
    )
    return result

demo = gr.Interface(fn=request, inputs="textbox", outputs="json")
    
demo.launch(share=True)