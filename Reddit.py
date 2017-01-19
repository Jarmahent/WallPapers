import praw
import Obot
import pyimgur
import urllib.parse
import string
import random
import urlArray
import time
from urllib import request
from PIL import Image
import sqlite3

keyWords = ['gallery', '/a/']


class get_image(object):

    def width(self):
        im = Image.open(self)
        width = im.size[0]
        return width

    def height(self):
        im = Image.open(self)
        height = im.size[1]
        return height

sub = 'wallpaper'
redd = "redd"
reddit = 'reddit'
jpg = 'jpg'
imgur = 'imgur'



print('Logging in')
r = praw.Reddit(Obot.app_id)
im = pyimgur.Imgur(Obot.client_id, Obot.client_secret)

def id_gen(size=9, chars=string.ascii_uppercase + string.digits):  #Create random ID
    return ''.join(random.choice(chars) for _ in range(size))




while True:
    print("--Sleeping for 30 seconds")
    time.sleep(30)

    submissions = r.get_subreddit(sub).get_random_submission()

    print('--Submission Found in ' + sub)
    print("--Submission.url: ", submissions.url)

    if submissions.url in urlArray.urllist:
        print("--This url has already been downloaded")
        continue

    print("--Adding url to array")
    urlArray.urllist.append(submissions.url)



    url = urllib.parse.unquote(submissions.url)
    #if url doesnt have jpg and doesnt have "gallery" or "/a/"
    if(not jpg in url and imgur in url and not "gallery" in url and not "/a/" in url):
        print("--Url without jpg format: ", url)
        jpgURL = submissions.url + ".jpg"
        print("--Remade url is: ", jpgURL)
        imgur_name2 = id_gen()
        newurl2 = jpgURL.split('/')[-1].split('.')[0]
        im.get_image(newurl2).download(path="C:\\Users\\KEVIN\\Pictures\\temp_pics", name=imgur_name2, overwrite=False, size=None)
        print("--Downloaded remade url")

    if jpg in url and imgur in url:


        newurl = url.split('/')[-1].split('.')[0]
        imgur_name = id_gen()
        temp_pic = imgur_name + ".jpg"
        print("--Downloading Image through Imgur")
        im.get_image(newurl).download(path="C:\\Users\\KEVIN\\Pictures\\temp_pics", name=imgur_name, overwrite=False, size=None)



    if reddit in url:
        reddit_gen = id_gen()
        reddit_pic = reddit_gen + ".jpg"
        print("\n" + "--Downloading through I.Reddit")
        request.urlretrieve(url, "C:\\Users\\KEVIN\\Pictures\\temp_pics\\" + reddit_pic)

    if not reddit in url and not redd in url and not imgur in url and jpg in url:
        print("--Not reddit or imgur but I can download the image")
        randomGen = id_gen()
        request.urlretrieve(url, "C:\\Users\\KEVIN\\Pictures\\temp_pics\\" + randomGen + ".jpg")
        print("--Downloaded", "This image ID is: ", randomGen)






















