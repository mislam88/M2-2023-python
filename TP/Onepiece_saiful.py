# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 16:55:19 2023

@author: hp
"""

from PIL import Image
import requests
import os 

HEADERS = {'user-agent': 'my-agent/1.0.1'}

def save_image(chapter, i):
    j = f'{i:02}'  
    
    pic_url = f'https://www.scan-vf.net/uploads/manga/one_piece/chapters/chapitre-{chapter}/{j}.webp'
    response = requests.get(pic_url, stream=True, headers=HEADERS)
    
    if not response.ok:
        return False
    
    # Save the webp image
    webp_filename = f'resultats/chapitre-{chapter}_{j}.webp'
    with open(webp_filename, "wb") as output:
        for block in response.iter_content(1024):
            if not block:
                break
            output.write(block)
    
    # Convert webp to png
    png_filename = f'resultats/chapitre-{chapter}_{j}.png'
    im = Image.open(webp_filename).convert('RGB')
    im.save(png_filename, 'png')
    
    return True

def main():
    chapter = 1  # starting chapter
    while True:
        i = 1  # reset page for each chapter
        while True:
            if not save_image(chapter, i):
                break  # no more pages for this chapter
            print(f"Processed Chapter {chapter} Page {i}")
            i += 1
        
        chapter += 1
       
if __name__ == "__main__":
    main()
'''
for particular chapters 

def main():
    for chapter in range(1, 51):  # iterating from chapter 1 to chapter 50
        i = 1  # start page for each chapter
        while True:
            if not save_and_convert_image(chapter, i):
                break  # no more pages for this chapter
            print(f"Processed Chapter {chapter} Page {i}")
            i += 1

if __name__ == "__main__":
    main()'''




