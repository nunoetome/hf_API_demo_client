from gradio_client import Client
import gradio as gr

DEBUG_MODE = True

client = Client("Nuno-Tome/API_demo_server")

def request(text):
    if DEBUG_MODE:
        gr.Markdown("client:" + str(client))
        gr.Markdown(f"## Requesting prediction for: {text}")
    result = client.echo(
		"Hello World",	# str  in 'text' Textbox component
        #text,
		api_name="/echo"
    )
    if DEBUG_MODE:
        gr.Markdown(f"## Prediction result: {result}")
        print(f"Prediction result: {result}")
    return result


io = gr.Interface(request, "textbox", "json")