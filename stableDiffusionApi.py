
import requests
import io
import base64
from PIL import Image, PngImagePlugin

url = "http://127.0.0.1:7860"

def setModel(modelName):
    option_payload = {
        "sd_model_checkpoint": modelName    
        #"dreamshaper_8.safetensors [879db523c3]"
    }

    response = requests.post(url=f'{url}/sdapi/v1/options', json=option_payload)

def generate(promptString, seed):

    payload = {
    "prompt": promptString,
    "steps": 20,
    "width": 512,
    "height": 512,
    "seed": seed
    }
   
    response = requests.post(url=f'{url}/sdapi/v1/txt2img', json=payload)

    r = response.json()

    return r

def saveImage(r, id):
     for i in r['images']:
        image = Image.open(io.BytesIO(base64.b64decode(i.split(",",1)[0])))

        png_payload = {
            "image": "data:image/png;base64," + i
        }
        response2 = requests.post(url=f'{url}/sdapi/v1/png-info', json=png_payload)

        pnginfo = PngImagePlugin.PngInfo()
        pnginfo.add_text("parameters", response2.json().get("info"))
        image.save("Output/"+str(id)+'.png', pnginfo=pnginfo) 
