import praw
import Obot
import pyimgur
import urllib.parse
import string
import random
from urllib import request
import time

keyWords = ['gallery', '/a/']

sub = 'wallpaper'
redd = "redd"
reddit = 'reddit'
jpg = 'jpg'
imgur = 'imgur'


print('Logging in')
r = praw.Reddit(
    client_id=Obot.app_id,
    client_secret=Obot.app_secret,
    user_agent=Obot.app_id
)


im = pyimgur.Imgur(Obot.client_id, Obot.client_secret)


def id_gen(size=9, chars=string.ascii_uppercase + string.digits):  # Create random ID
    return ''.join(random.choice(chars) for _ in range(size))


while True:


    submissions = r.subreddit(sub).random()

    print('Submission Found in ' + sub)
    print("Submission.url: ", submissions.url)

    url = urllib.parse.unquote(submissions.url)
    # if url doesnt have jpg and doesnt have "gallery" or "/a/"
    if (not jpg in url and imgur in url and not "gallery" in url and not "/a/" in url):
        print("Url without jpg format: ", url)
        jpgURL = submissions.url + ".jpg"
        print("Remade url is: ", jpgURL)
        print("Its not in here!")
        imgur_name2 = id_gen()
        ImageDbIn = open("imagedb.txt").read()
        if(jpgURL in ImageDbIn):
            print("URL has already been downloaded, restarting.")
            break
        else:
            print("Appending url to DB")
            ImageDbOut = open("imagedb.txt", "a")
            ImageDbOut.write(jpgURL + "\n")
            newurl2 = jpgURL.split('/')[-1].split('.')[0]
            im.get_image(newurl2).download(path="C:\\Users\\KEVIN\\Pictures\\pics", name=imgur_name2, overwrite=False, size=None)
            print("Downloaded remade url")


    #download image through Imgur
    if jpg in url and imgur in url:

        newurl = url.split('/')[-1].split('.')[0]
        imgur_name = id_gen()
        print("New URL detected, storing.")
        temp_pic = imgur_name + ".jpg"
        print("\n" + 'Downloading Image through Imgur', "\n")
        ImageDbIn = open("imagedb.txt").read()
        if(newurl in ImageDbIn):
            print("URL has already been downloaded, restarting.")
            break
        else:
            print("Appending url to DB")
            ImageDbOut = open("imagedb.txt", "a")
            ImageDbOut.write(newurl + "\n")
            im.get_image(newurl).download(path="C:\\Users\\KEVIN\\Pictures\\pics", name=imgur_name,
                                          overwrite=False,
                                          size=None)

    if reddit in url:
        reddit_gen = id_gen()
        reddit_pic = reddit_gen + ".jpg"
        print("\n" + "Downloading through I.Reddit")
        print("New URL detected, storing.")

        ImageDbIn = open("imagedb.txt").read()
        if(ImageDbIn in url):
            print("URL has already been downloaded, restarting.")
            break
        else:
            print("Appending url to DB")
            ImageDbOut = open("imagedb.txt", "a")
            ImageDbOut.write(url + "\n")
            request.urlretrieve(url, "C:\\Users\\KEVIN\\Pictures\\pics\\" + reddit_pic)

    if not reddit in url and not redd in url and not imgur in url and jpg in url:
        print("Not reddit or imgur but I can download the image")
        randomGen = id_gen()
        print("New URL detected, storing.")
        ImageDbIn = open("imagedb.txt").read()
        if(url in ImageDbIn):
            print("URL has already been downloaded, restarting.")
            break
        else:
            print("Appending url to DB")
            ImageDbOut = open("imagedb.txt", "a")
            ImageDbOut.write(url + "\n")
            request.urlretrieve(url, "C:\\Users\\KEVIN\\Pictures\\pics\\" + randomGen + ".jpg")
            print("Downloaded", "This image ID is: ", randomGen)

    print("Waiting 30 seconds")
    x = 0
    for x in range(30):
        print(x + 1)
        time.sleep(1)