import praw
import Obot
import pyimgur
import urllib.parse
import string
import random
import time
from urllib import request





print('Logging in')
r = praw.Reddit(Obot.app_id)
im = pyimgur.Imgur(Obot.client_id, Obot.client_secret)

def id_gen(size=9, chars=string.ascii_uppercase + string.digits):  #Create random ID
    return ''.join(random.choice(chars) for _ in range(size))




while True:

    sub = 'HighRes'
    submissions = r.get_subreddit(sub).get_random_submission()
    print('Submission Found in ' + sub)

    url = urllib.parse.unquote(submissions.url)
    reddit = 'reddit'
    jpg = 'jpg'
    imgur = 'imgur'
    if jpg in url and imgur in url:
        newurl = url.split('/')[-1].split('.')[0]
        print('Downlading Image through Imgur')
        im.get_image(newurl).download(path="C:\\Users\\KEVIN\\Pictures\\PyImgur", name=id_gen(), overwrite=False, size=None)



        #Space
    if reddit in url:
        print("Downloading through I.Reddit")
        request.urlretrieve(url, "C:\\Users\\KEVIN\\Pictures\\PyImgur" + id_gen() + '.jpg')















