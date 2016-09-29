import praw
import Obot
import time
import pyimgur
import urllib.parse
import string
import random
import urllib



print('Loging in')
r = praw.Reddit(Obot.app_id)

im = pyimgur.Imgur(Obot.client_id, Obot.client_secret)

def id_gen(size=9, chars=string.ascii_uppercase + string.digits):  #Create random ID
    return ''.join(random.choice(chars) for _ in range(size))




while True:


    submissions = r.get_subreddit('pics').get_random_submission()
    url = urllib.parse.unquote(submissions.url)
    reddit = 'i.reddi'
    jpg = 'jpg'
    imgur = 'imgur'
    if jpg in url and imgur in url:
        newurl = url.split('/')[-1].split('.')[0]
        im.get_image(newurl).download(path="C:\\Users\\KEVIN\\Pictures\\PyImgur", name=id_gen(), overwrite=False, size=None)
        time.sleep(30)











