import pygame
from PIL import Image, ImageDraw
import PIL.Image
import os.path
import math
import random
import time
import RPi.GPIO as GPIO, time, os, subprocess,shlex
pygame.init()
path = "/home/pi/SailingPhotos"
infoObject = pygame.display.Info()
screen = pygame.display.set_mode((infoObject.current_w,infoObject.current_h), pygame.FULLSCREEN)  # Full screen 
def set_demensions(img_w, img_h):
    # Note this only works when in booting in desktop mode. 
	# When running in terminal, the size is not correct (it displays small). Why?

    # connect to global vars
    global transform_y, transform_x, offset_y, offset_x

    # based on output screen resolution, calculate how to display
    ratio_h = (infoObject.current_w * img_h) / img_w 

    if (ratio_h < infoObject.current_h):
        #Use horizontal black bars
        #print "horizontal black bars"
        transform_y = ratio_h
        transform_x = infoObject.current_w
        offset_y = (infoObject.current_h - ratio_h) / 2
        offset_x = 0
    elif (ratio_h > infoObject.current_h):
        #Use vertical black bars
        #print "vertical black bars"
        transform_x = (infoObject.current_h * img_w) / img_h
        transform_y = infoObject.current_h
        offset_x = (infoObject.current_w - transform_x) / 2
        offset_y = 0
    else:
        #No need for black bars as photo ratio equals screen ratio
        #print "no black bars"
        transform_x = infoObject.current_w
        transform_y = infoObject.current_h
        offset_y = offset_x = 0
def getcropdim(width,height):
    if int(width/6)>(height/4):#This only works if height or width fits in the surface
        step = int(height/4)
    else:
        step = int(width/6)
    left = (width/2)-(3*step)
    top= (height/2)-(2*step)
    width = (6*step)
    height = (4*step)
    print(f"DIMENSIONS left: {left} top: {top} width: {width} height: {height}")
    left = int(math.floor(left))
    top = int(math.floor(top))
    width =math.floor(width)
    height = math.floor(height)
    return left, top, width,height

def resizedim(x,y):
    if int(x/6)*2>(y/2):
        step = int(y/4)
    else:
        step = int(x/6)
    top2 = (y/2)-(2*step)	
    left2 = (x/2)-(3*step)
    right2 = (x/2)+(3*step)
    bottom2 = (y/2)+(2*step)
    width2 = left2+right2
    height2 = top2+bottom2
    return width2,height2
def show_image(image_path,screen):
    img = pygame.image.load(image_path)
    img = img.convert()
    screen.fill(pygame.Color("black"))
    x,y = screen.get_size()##no reratio needed, just resize
    width = int(img.get_width())
    height = int(img.get_height())
    left, top, width,height = getcropdim(width,height)
    cropimg1 = img.subsurface((left,top,width,height))#puts it into correct ratio
    width2,height2 = resizedim(x,y)
    width2 =int(width2)
    height2 =int(height2)
        # Make the image full screen
    cropimg = pygame.transform.scale(cropimg1, (width2,height2))
    width3 = int(cropimg.get_width())
    height3 = int(cropimg.get_height())
    print(f"Type x{type(x)} and type y{type(y)}")
    screen.blit(cropimg,((x/2)-(width3/2),(y/2)-(height3/2)))
    pygame.display.flip()
piclist =[]
def updatepics(path,piclist):
    newimglist = []
    dir_list = os.listdir(path)
    for i in range(0,len(dir_list)):
        #print(dir_list[i][-3:])
        if dir_list[i] not in piclist:
            if dir_list[i][-3:]=="jpg" or dir_list[i][-3:]=="JPG" or dir_list[i][-3:]=="PNG" or dir_list[i][-3:]=="png":
                piclist.append(dir_list[i])
                newimglist.append(dir_list[i])
    return piclist,newimglist
i=0
j=0
##SHow the 5 most recent pics first
piclist,newimglist = updatepics(path,piclist)
show_image((path+"/"+str(piclist[i])),screen)

for event in pygame.event.get():   
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
            print("escape Key Pressed Exiting..")
            pygame.quit()

