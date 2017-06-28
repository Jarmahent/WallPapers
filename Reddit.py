import praw
import Obot
import pyimgur
import urllib.parse
import string
import random
from urllib import request
import time
import os



print('Logging in')
r = praw.Reddit(
    client_id=Obot.app_id,
    client_secret=Obot.app_secret,
    user_agent=Obot.app_id
)

im = pyimgur.Imgur(Obot.client_id, Obot.client_secret)


def id_gen(size=9, chars=string.ascii_uppercase + string.digits):  # Create random ID
    return ''.join(random.choice(chars) for _ in range(size))
# Create path for user in Pictures
Localpath = os.path.expanduser("~")
if not os.path.exists("{}\Pictures\PyPics".format(Localpath)):
    os.makedirs("{}\Pictures\PyPics".format(Localpath))
    print("Path does not exist, creating folder.")

while True:
    ImageDbIn = open("imagedb.txt").read()
    print("Pick a subreddit: ")
    sub = input()

    try:
        submissions = r.subreddit(sub).random()
    except:
        print("Not a subreddit try again.")
        continue



    print('Submission Found in {}'.format(sub))
    print("Submission.url: ", submissions.url)

    url = urllib.parse.unquote(submissions.url)
    # if url doesnt have jpg and doesnt have "gallery" or "/a/"
    if not ".jpg" in url and "imgur" in url and not "gallery" in url and not "/a/" in url:
        print("Url without jpg format: ", url)
        jpgURL = submissions.url + ".jpg"
        print("Remade url is: ", jpgURL)
        imgur_name2 = id_gen()
        if jpgURL in ImageDbIn:
            print("URL has already been downloaded, restarting.")
            continue
        else:
            print("Appending url to DB")
            ImageDbOut = open("imagedb.txt", "a")
            ImageDbOut.write(jpgURL + "\n")
            newurl2 = jpgURL.split('/')[-1].split('.')[0]
            im.get_image(newurl2).download(path="{}\Pictures\PyPics".format(Localpath), name=imgur_name2, overwrite=False, size=None)
            print("Downloaded remade url")


    # download image through Imgur
    if ".jpg" in url and "imgur" in url:

        newurl = url.split('/')[-1].split('.')[0]
        imgur_name = id_gen()
        print("New URL detected, storing.")
        temp_pic = imgur_name + ".jpg"
        print('{} Downloading Image through Imgur {} '.format("\n", "\n"))
        if(newurl in ImageDbIn):
            print("URL has already been downloaded, restarting.")
            continue
        else:
            print("Appending url to DB")
            ImageDbOut = open("imagedb.txt", "a")
            ImageDbOut.write(newurl + "\n")
            im.get_image(newurl).download(path="{}\Pictures\PyPics".format(Localpath), name=imgur_name,
                                          overwrite=False,
                                          size=None)
    # Download I.reddit url
    if "reddit" in url:
        reddit_gen = id_gen()
        reddit_pic = reddit_gen + ".jpg"
        print("\n" + "Downloading through I.Reddit")
        print("New URL detected, storing.")
        if(ImageDbIn in url):
            print("URL has already been downloaded, restarting.")
            continue
        else:
            print("Appending url to DB")
            ImageDbOut = open("imagedb.txt", "a")
            ImageDbOut.write(url + "\n")
            request.urlretrieve(url, "{}\Pictures\PyPics\{}".format(Localpath, reddit_pic))

    # Download URL that is not reddit or imgur but has jpg extenstion
    if not "reddit" in url and not "redd" in url and not "imgur" in url and ".jpg" in url:
        print("Not reddit or imgur but I can download the image")
        randomGen = id_gen()
        print("New URL detected, storing.")
        if(url in ImageDbIn):
            print("URL has already been downloaded, restarting.")
            continue
        else:
            print("Appending url to DB")
            ImageDbOut = open("imagedb.txt", "a")
            ImageDbOut.write(url + "\n")
            request.urlretrieve(url, "{}\Pictures\PyPics\{}{}".format(Localpath, randomGen, ".jpg"))
            print("Downloaded", "This image ID is: ", randomGen)

    # Download I.redd url
    if"redd" in url and ".jpg" in url:
        print("i.redd Url detected, trying to download...")
        randomGen = id_gen()
        if(url in ImageDbIn):
            print("URL has already been downloaded, restarting.")
            continue
        else:
            print("Appending URL to database")
            ImageDbOut = open("imagedb.txt", "a")
            ImageDbOut.write(url + "\n")
            request.urlretrieve(url, "{}\Pictures\PyPics\{}{}".format(Localpath, randomGen, ".jpg"))


    # Wait 10 sec


    print("Waiting 10 seconds")
    x = 0
    for x in range(10):
        print(x + 1)
        time.sleep(1)