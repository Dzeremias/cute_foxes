import requests 
import ast
import os.path


resp = requests.get("https://randomfox.ca/floof")

respdict = ast.literal_eval(resp.text)
imglink = respdict.get("image", "no link")
imglink = imglink.replace("\\", "")
filename = "foxy"+str(imglink.rsplit("/", 1)[1])

imageresp = requests.get(imglink)

if os.path.exists(filename):
    print("This cute little foxy was already downloaded")
    
else:
    print ("Cute Foxy downloaded!")
    with open(filename, "wb") as file:
        print (f"Cute Foxy saved as {filename}")
        file.write(imageresp.content)
    