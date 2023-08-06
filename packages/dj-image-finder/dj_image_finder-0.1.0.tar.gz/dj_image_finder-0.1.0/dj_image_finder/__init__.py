import click
import sys
import urllib.request
import climage
import os
import keyboard
from serpapi import GoogleSearch

@click.command()
@click.option('--name', default="apple", help='change search keyword')  

def image(name):
    while True:
        params = {
                "api_key": "38a97aad2c5d1e37ceb5ff7d656d2e66722b552aff12c37ba3f5f0c6677e840b",
                "device": "desktop",
                "engine": "google",
                "q": name,
                "google_domain": "google.com",
                "tbm": "isch"
                }

        def print_image(file):
            try:
                try:
                    os.system("viu {}".format(file))
                except:
                    output = climage.convert(file)
                    print(output)
            except:
                print("image is unavailable")

        
        def get_filetype(link):
            if "png" in link:
                return "png"
            elif "jpg" or "jpeg" in link:
                return"jpg"
        
        def create_file_name(URL):
            image_name = input("\nEnter the image name: ")[1:]
            image_location = input("Enter the saving location: ")
            file_type = "."  
            file_type += format(get_filetype(URL))
            return "{}{}{}".format(image_location, image_name, file_type)
            

        def download_image(URL, name):
            urllib.request.urlretrieve(URL, name)
            print("image saved successfully")
            
            

        x = []
        search = GoogleSearch(params)
        results = search.get_dict()

        for i in results['images_results']:
            try:
                x.append(i['original'])
            except KeyError:
                pass
        UI = input("\nEnter the number between 0~{}: ".format(len(x)-1))
        
        if len(UI) >= 2:
            UI = UI[1:]

        URL = x[int(UI)]

        if get_filetype(URL) == "png":
            urllib.request.urlretrieve(URL, "sample.png")
            print_image("sample.png")
        elif get_filetype(URL) == "jpg":
            urllib.request.urlretrieve(URL, "sample.jpg")
            print_image("sample.jpg")
        else:
            print("image unavailable")

        print("q: exit  r: search again  s: change keyword   d: download image")
        event = keyboard.read_event()
        e_type = event.event_type
        keyd = keyboard.KEY_DOWN
        n = event.name
        while True:
            if e_type == keyd and n == 'q':
                sys.exit()
            elif e_type == keyd and n == 's':
                name = input("Enter the word to search: ")[1:]
                break
            elif e_type == keyd and n == 'r':
                break
            elif e_type == keyd and n == 'd':
                download_image(URL, create_file_name(URL))
                sys.exit()



