#Author : Thisara Chathuranga
#Date : 2020/11/26
#Python program to sort images and rotate all of the images in the directory by 15 degrees till 180 and make a copy each time 
import os 
from PIL import Image
import fnmatch
import sys

import time

from progressbar import AnimatedMarker, Bar, BouncingBar, Counter, ETA, \
    AdaptiveETA, FileTransferSpeed, FormatLabel, Percentage, \
    ProgressBar, ReverseBar, RotatingMarker, \
    SimpleProgress, Timer, UnknownLength

#variables used
COUNT = 1
num = 1
num2 = 1
Number_Of_Files=0
i=0
j=0
newsize = (1280,720)

#path name variablle 
#edit the following path to suit your directory  
pathdir = r'add your path here'  
os.chdir(pathdir) 


  
# Function to increment count  
# to make the files sorted. 
def increment(): 
    global COUNT 
    COUNT = COUNT + 1

# Function to increment count  
# to make the files sorted.     
def increment1(): 
    global num 
    num = num + 1

# Function to increment count  
# to make the files sorted.     
def increment2(): 
    global num2 
    num2 = num2 + 1

#Counting number of photos  
for file in os.listdir(pathdir):
    if fnmatch.fnmatch(file, '*.jpg'):#change the *.png to any kind of image format
        Number_Of_Files=Number_Of_Files+1
maxprogress = Number_Of_Files*11

#sort all the images in format of Imagex_y.jpg  
print('Sorting and Renaming:')
pbar = ProgressBar(widgets=[Percentage(), Bar()], maxval=Number_Of_Files).start()
for f in os.listdir(): 
    f_name,f_ext = os.path.splitext(f) 
    f_name = "Image" + str(COUNT) + "_0" 
    new_name = '{}{}'.format(f_name, f_ext) 
    os.rename(f, new_name)
    increment() 
    j=j+1
    pbar.update(j)
pbar.finish()

print()
print('Resizing:')
pbar = ProgressBar(widgets=[Percentage(), Bar()], maxval=Number_Of_Files+1).start()#Progress bar implementation
for x in range(1, Number_Of_Files+1):
    im1 = Image.open("Image" + str(num) + "_0.jpg")
    im1 = im1.resize(newsize)
    im1.save('Image' + str(num)+'_0.jpg')
    increment1()
pbar.finish()
num=1
    

print()
print('Rotating:')
pbar = ProgressBar(widgets=[Percentage(), Bar()], maxval=maxprogress).start()#Progress bar implementation
for x in range(1, Number_Of_Files+1):
    im = Image.open("Image" + str(num) + "_0.jpg")#Use the correct image format
    
    #rotate image
    for y in range(1,12):
        angle = 15*num2
        out = im.rotate(angle, expand=False)#make this True to fit image
        out.save('Image' + str(num)+'_'+str(num2) +'.jpg')#Use the correct image format
        increment2()
        i=i+1
        pbar.update(i)
    num2=1
    increment1()   
pbar.finish() 
sys.exit() 
