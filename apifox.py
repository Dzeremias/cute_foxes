import requests 
import ast
import os.path

#First API call. Response contains an img link + some other stuff
print("Getting a link to cute fox...")
resp = requests.get("https://randomfox.ca/floof") 

#Get the link and file name from the response and format the stuff
respdict = ast.literal_eval(resp.text)
imglink = respdict.get("image", "no link")
imglink = imglink.replace("\\", "")
filename = "foxy"+str(imglink.rsplit("/", 1)[1])

#Downloading the actual picture
imageresp = requests.get(imglink)

if os.path.exists(filename):
    print("This cute little foxy was already downloaded")
    
else:
    print ("Cute Foxy downloaded!")
    with open(filename, "wb") as file:
        print (f"Cute Foxy saved as {filename}")
        file.write(imageresp.content)
    
print("Press anything to exit...")
input()