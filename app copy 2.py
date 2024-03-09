import gradio as gr
from gradio_client import Client

MESAGE_HEADER = """
# API Demo (Client component)
Welcome to my simple demonstration of the gradio potential as an API.

It is made of 2 components: *API_demo_server* and *API_demo_client*.

Server component: [Nuno-Tome/API_demo_server](Nuno-Tome/aPI_demo_server)
Client component: [Nuno-Tome/API_demo_client](Nuno-Tome/aPI_demo_client)

**Just write you message and watch it be returned by the server.**   
                
"""



MESAGE_BMC = """
## If you want to support me, you can buy me a coffee:
    
    [![Buy me a coffee](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/nunotome)
    """
    
# Print the message header for "By me a coffee" link
def print_bmc():

    bmc_link = "https://www.buymeacoffee.com/nuno.tome"
    image_url = "https://helloimjessa.files.wordpress.com/2021/06/bmc-button.png?w=" # Image URL
    #image_size = "150px" # Image size
    #image_link_markdown = f"[![Buy Me a Coffee]({image_url})]({bmc_link})"
    image_link_markdown = "[![Buy Me a Coffee]({image_url})]({bmc_link})"

    gr.Markdown("""
                [![Buy Me a Coffee]({image_url})]({bmc_link})
                """)
    # Buy me a Coffee Setup

   
    


client = Client("Nuno-Tome/API_demo_server")
DEBUG_MODE = True


def request(text):
    
    gr.Markdown(
    """
    # Hello World!
    Start typing below to see the output.
    """)
    
    result = client.predict(
        text,
		api_name="/predict"
    )
    return result

demo = gr.Interface(fn=request, inputs="textbox", outputs="json")
    
demo.launch(share=True)