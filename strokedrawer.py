#!/usr/bin/env python



from PIL import Image, ImageDraw
from argparse import ArgumentParser
import sys

#This script opens up a temp file and an image file existing in its
#directory and uses ImageDraw to add line segments from the temp
#file to the image file

if __name__ == "__main__":
    
    #open the image file
    pic = Image.new('1',(5000,5000),color='white')

    #set up a drawing context
    draw = ImageDraw.Draw(pic)
   
    for lines in sys.stdin.readlines():
        lines = lines.strip().split()
        lines = [ float(x)/10 for x in lines ]
        draw.line(lines,width=3)
        
    
    pic.save("out.png")
