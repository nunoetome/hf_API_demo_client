from gradio_client import Client
import gradio as gr

client = Client("Nuno-Tome/API_demo_server")

def request(text):
    result = client.predict(
		"Hello World",	# str  in 'text' Textbox component
		api_name="/predict"
    ) 
    return result


io = gr.Interface(request, "textbox", "json")