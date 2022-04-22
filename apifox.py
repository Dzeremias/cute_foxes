import requests 
import ast
import os.path

while True:
    userinp = input("How many foxes would you like to download? (q = quit): ")
    if userinp == "q":
        break
    try:
        foxnumber = int(userinp)
    except ValueError:
        print("Invalid input")
        continue
    
    for i in range(foxnumber):
        resp = requests.get("https://randomfox.ca/floof/")
        respdict = ast.literal_eval(resp.text)
        imglink = respdict.get("image", "no link")
        imglink = imglink.replace("\\", "")
        filename = "foxy"+str(imglink.rsplit("/", 1)[1])

        imageresp = requests.get(imglink)

        if os.path.exists(f"zapifox/{filename}"):
            print(f"{filename} was already downloaded")
            
        else:
            print ("New cute Foxy downloaded!")
            with open(f"zapifox/{filename}", "wb") as file:
                print (f"Cute Foxy saved as {filename}")
                file.write(imageresp.content)
        