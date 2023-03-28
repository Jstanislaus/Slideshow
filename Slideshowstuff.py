import tkinter as tk
from tkinter import *
from PIL import Image
from PIL import ImageTk
import os
import time
import os.path
import datetime
import time
from datetime import date
import RPi.GPIO as GPio, time, os, shlex
#monthdic = { "Jan":"01","Feb":"02", "Mar": "03","Apr":"04", "May":"05", "Jun":"06", "Jul":"07", "Aug":"08",
# "Sep":"09",  "Oct":"10", "Nov": "11", "Dec":"12"}
# adjust window
win=tk.Tk()
  
# loading the images

screen_width = win.winfo_screenwidth()
screen_height = win.winfo_screenheight()
win.geometry(str(screen_width)+"x"+str(screen_height))
#####
#resize
#######
#find divisor
path = "/home/pi64/Slideshow"
#path = input("Please give the directory location of your files")
print("Resizing photos...")
dir_list = os.listdir(path)
imgarray = []
for i in range(0,len(dir_list)):
    if dir_list[i][-3:]=="jpg" or dir_list[i][-3:]=="JPG" or dir_list[i][-3:]=="PNG" or dir_list[i][-3:]=="png":
        img = Image.open(str(dir_list[i]))
        w,h = img.size
        ratio = h/w
        if ratio > 1:
            resized_image = img.resize((int(screen_width),int(ratio * screen_width)))
        else:
            ratio = w/h
            resized_image = img.resize((int(screen_height * ratio),int(screen_height)))
        img = ImageTk.PhotoImage(resized_image)
        imgarray.append(img)
#check current date
try:
    modified_time = os.path.getmtime(path+"/"+dir_list[0])
    convert_time = time.ctime(modified_time)
    current_time = datetime.datetime.now() 
    array = convert_time.split(" ")
    timearray = array[3].split(":")
    year = int(array[4])
    month = int(monthdic[array[1]])
    day = int(array[2])
    hour = int(timearray[0])
    minute = int(timearray[1])
    second = int(timearray[2])
    current_time = str(current_time)
    timearray = current_time.split("-")
    timearray[1] = int(timearray[1])
    #if int(timearray[2][:1])==int(day) and int(timearray[1])==int(month) and int(timearray[0])==int(year):
    #    hourdiff = abs(int(timearray[2][3:5])-hour)
    #    mindiff = abs(int(timearray[2][6:8])-minute)
    #    second_diff = abs(int(timearray[2][9:11])-second)
    #    greeting = tk.Label(text="These photos were taken today "+str(hourdiff)+" hour/s, "+str(mindiff)+" minute/s and "+str(second_diff)+" second/s ago in fact!",font = ('Times',24))
    #elif int(timearray[1])==int(month) and int(timearray[0])==int(year):
   #     daydiff = abs(int(timearray[2][:2])-int(day))
  #      greeting = tk.Label(text="These photos were taken this month, in fact "+str(daydiff)+" day/s ago!",font = ('Times',24))
  #  elif int(timearray[0])==int(year):
  #      month_diff = abs(int(timearray[1])-int(month))
  #      greeting = tk.Label(text="This year, "+str(month_diff)+" month/s ago",font = ('Times',24))
  #  else:
  #      yeardiff = abs(int(timearray[0])-int(year))
  #      greeting = tk.Label(text="This was taken "+str(yeardiff)+" ago",font = ('Times',24))
  #  greeting.pack()
except:
    pass
l=Label()
l.pack()
os.system('cls' if os.name == 'nt' else 'clear')
print("Checking files...")
#find number of files that will be in slideshow

def find_all(dir_list):
    counter = 0
    for i in range(0,len(dir_list)):
        if dir_list[i][-3:] == "jpg" or dir_list[i][-3:] == "JPG" or dir_list[i][-3:]=="png" or dir_list[i][-3:]=="PNG":
            counter +=1
        else:
            pass
    return counter

count = find_all(dir_list)
print(count)
os.system('cls' if os.name == 'nt' else 'clear')
#speed = int(input("How quickly would you like to run the photos? (out of 10 from fast to slow)"))
#speed = speed*250
speed = 900
x=1
def move():
    global x
    if x == count+1:
        x = 1
    else:
        l.config(image=imgarray[x-1])
    x = x+1
    win.after(800+speed, move)  
# calling the function
i=0
while True:
    if i%50 == 5:
        cmdline = "rsync -avz -e ssh pi@192.168.1.155:Slideshow/ Slideshow" 
        args = shlex.split(cmdline)
        print(args)
        time.sleep(0.2)
        print(shlex.split("stanislaus"))
    move()
    win.mainloop()
    i+=1
