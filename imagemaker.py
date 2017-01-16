#!/usr/bin/env python

from PIL import Image
from argparse import ArgumentParser

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("--filename", action = "store", dest = "filename", help = "name of this image file", required = True)
    o = parser.parse_args()

    #Creates a 50x50 image object that's initialized to all white
    pic = Image.new(mode='1',size=(50,50),color='white')
    pic.save(o.filename+".jpg","JPEG")



