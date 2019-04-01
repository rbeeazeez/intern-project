# import the json library, decodes JSON text into python obj
import json
# A URL library is required to store data retrieved from the Api and store to local system
import urllib.request
import os

data = urllib.request.urlopen("https://api.unsplash.com/photos/random?client_id=0a276d64b77e207e5a38f13427cdd87dd21b8\
15fb281c1d046d1bc82c05d468c").read()
output = json.loads(data.decode('utf-8'))

tem_file_name = "/home/rbeeazeez/PycharmProjects/intern/background.jpg"
img_dir_link = output["urls"]["full"]

print("Downloading image...")
urllib.request.urlretrieve(img_dir_link, tem_file_name)
print("Setting image as wallpaper")


os.system("gsettings set org.gnome.desktop.background picture-uri file:///home/rbeeazeez/PycharmProjects/intern/backgro\
und.jpg")



