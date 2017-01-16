#!/usr/bin/env python



from PIL import Image, ImageDraw
from argparse import ArgumentParser

#This script opens up a temp file and an image file existing in its
#directory and uses ImageDraw to add line segments from the temp
#file to the image file

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("--intext", action = "store", dest = "intext", help = "file with lines to draw", required = True)
    parser.add_argument("--filename", action = "store", dest = "filename", help = "name of image file to draw on", required = True)
    o = parser.parse_args()
    
    #open the image file
    #pic = Image.open(o.filename+".jpg")
    #set up a drawing context

    pic = Image.new('1',size = (10000,10000),color='white')
    draw = ImageDraw.Draw(pic)
    #draw.line((0,0) + pic.size, fill = 128)
    draw.line([7726,2911,7726,2911,7726,2911,7726,2911,7726,2937,7699,2963,7699,3043,7673,3175],fill='red')
    pic.save('temp.png', 'PNG')
    #draw.line([7726 2911 7726 2911 7726 2911 7726 2911 7726 2937 7699 2963 7699 3043 7673 3175 7673 3360 7646 3572 7646 3836 7646 4075 7673 4313 7726 4498 7752 4683 7805 4789 7858 4895 7885 4974 7911 5027 7911 5053 7911 5080 7911 5080 7911 5080 7911 5027 7938 4974 7964 4868 8017 4762 8070 4604 8123 4472 8202 4339 8282 4260 8335 4207 8413 4180 8466 4207 8494 4233 8546 4287 8598 4365 8625 4472 8651 4604 8678 4736 8678 4868 8651 4974 8625 5080 8598 5133 8546 5212 8466 5239 8388 5265 8307 5292 8229 5292 8123 5292 8043 5265 7964 5265 7911 5239 7858 5239 7832 5212 7805 5212],fill=rgb(0,0,0))
    #open input text file
    #intext = open(o.intext,'r')

    #for coordinates in intext:
    #    draw.line(coordinates,fill=rgb(0,0,0))

