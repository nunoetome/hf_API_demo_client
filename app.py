import gradio as gr
from gradio_client import Client

client = Client("Nuno-Tome/API_demo_server")
DEBUG_MODE = True


def request(text):
    #result = client.echo(text, api_name="/predict")
    #return result
    result = client.predict(
		"Hello!!",	# str  in 'text' Textbox component
		api_name="/predict"
    )
    return result

demo = gr.Interface(fn=request, inputs="textbox", outputs="textbox")
    
demo.launch(share=True)