from gradio_client import Client
import gradio as gr

DEBUG_MODE = True

client = Client("Nuno-Tome/API_demo_server")

def request(text):
    if DEBUG_MODE:
        print(f"Client: {client}")
        print(f"Requesting prediction for: {text}")
    result = client.predict(
		#"Hello World",	# str  in 'text' Textbox component
        text,
		api_name="/predict"
    )
    if DEBUG_MODE:
        print(f"Prediction result: {result}")
    return result


io = gr.Interface(request, "textbox", "json")