import praw
import Obot
import pyimgur
import urllib.parse
import string
import webbrowser
import random
import time
from urllib import request
from PIL import Image
import os, glob



class get_image(object):

    def width(self):
        im = Image.open(self)
        width = im.size[0]
        return width

    def height(self):
        im = Image.open(self)
        height = im.size[1]
        return height









print('Logging in')
r = praw.Reddit(Obot.app_id)
im = pyimgur.Imgur(Obot.client_id, Obot.client_secret)

def id_gen(size=9, chars=string.ascii_uppercase + string.digits):  #Create random ID
    return ''.join(random.choice(chars) for _ in range(size))




while True:

    sub = 'pics'
    submissions = r.get_subreddit(sub).get_random_submission()
    print('Submission Found in ' + sub)

    url = urllib.parse.unquote(submissions.url)
    reddit = 'reddit'
    jpg = 'jpg'
    imgur = 'imgur'

    if jpg in url and imgur in url:


        newurl = url.split('/')[-1].split('.')[0]
        imgur_name = id_gen()
        temp_pic = imgur_name + ".jpg"
        print( "\n" + 'Downloading Image through Imgur')
        im.get_image(newurl).download(path="C:\\Users\\KEVIN\\Pictures\\temp_pics", name=imgur_name, overwrite=False, size=None)

        if(get_image.width("C:\\Users\\KEVIN\\Pictures\\temp_pics\\" + temp_pic) < 3000):
            print("Image is not 4K" + "\n")
            print("Image resolution is: " + str(get_image.width("C:\\Users\\KEVIN\\Pictures\\temp_pics\\" + temp_pic)) + "x" + str(get_image.height("C:\\Users\\KEVIN\\Pictures\\temp_pics\\" + temp_pic)))
            print("Removing Image" + "\n")

            os.remove("C:\\Users\\KEVIN\\Pictures\\temp_pics\\" + temp_pic)


        elif(get_image.width("C:\\Users\\KEVIN\\Pictures\\temp_pics\\" + reddit_pic) >= 3000):
            print("Moving Image to /Pyimgur/")
            os.rename("C:\\Users\\KEVIN\\Pictures\\temp_pics\\" + reddit_pic, "C:\\Users\\KEVIN\\Pictures\\Pyimgur\\" + reddit_pic + "\n")

    if reddit in url:
        reddit_gen = id_gen()
        reddit_pic = reddit_gen + ".jpg"
        print("\n" + "Downloading through I.Reddit")
        request.urlretrieve(url, "C:\\Users\\KEVIN\\Pictures\\temp_pics\\" + reddit_pic)


        if(get_image.width("C:\\Users\\KEVIN\\Pictures\\temp_pics\\" + reddit_pic) < 3000):
            print("Image is not 4K" + "\n")
            print("Image resolution is: " + str(get_image.width("C:\\Users\\KEVIN\\Pictures\\temp_pics\\" + reddit_pic)) + "x" + str(get_image.height("C:\\Users\\KEVIN\\Pictures\\temp_pics\\" + reddit_pic)))
            print('Removing Image' + "\n")
            os.remove("C:\\Users\\KEVIN\\Pictures\\temp_pics\\" + reddit_pic)


        elif(get_image.width("C:\\Users\\KEVIN\\Pictures\\temp_pics\\" + reddit_pic) >= 3000):
            print("Moving Image to /Pyimgur/")
            os.rename("C:\\Users\\KEVIN\\Pictures\\temp_pics\\" + reddit_pic, "C:\\Users\\KEVIN\\Pictures\\Pyimgur\\" + reddit_pic)

















