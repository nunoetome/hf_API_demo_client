from gradio_client import Client

client = Client("Nuno-Tome/API_demo_server")
result = client.predict(
		"Hello!!",	# str  in 'text' Textbox component
		api_name="/predict"
)
print(result)